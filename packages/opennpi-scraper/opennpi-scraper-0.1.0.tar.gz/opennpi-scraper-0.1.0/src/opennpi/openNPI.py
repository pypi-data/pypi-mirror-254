import requests
from bs4 import BeautifulSoup
import re


class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla5.0 (Windows NT 10.0; Win64; x64; rv107.0) Gecko20100101 Firefox107.0",
                "Accept": "texthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,;q=0.8",
                "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "1",
            }
        )
        self.banned_headers = ["Improve Information", "Dataset Information"]

    def __get_page_detail(self, link):
        # Performs a GET request to the specified URL and parses the response content with BeautifulSoup.
        response = self.session.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        # Checks if there was a redirection from the original URL, indicating the NPI might not exist.
        if response.url != link:
            messageError = "The NPI does not exist."
            raise Exception(messageError)

        # Extracts the main header (name) of the provider or doctor from the page.
        name = soup.find("h1").text.strip()
        information = []
        # Finds all panels (sections) on the page to extract detailed information.
        panels = soup.find_all("div", class_="panel")

        for panel in panels:
            panel_info = {}
            header = panel.find("h2")
            description = panel.find("p", class_="lead")

            # Extracts the header and description, skipping any panels with banned headers.
            if header:
                header = header.text.strip()

                if header in self.banned_headers:
                    continue
                panel_info["header"] = header

            if description:
                panel_info["description"] = description.text.strip()

            # Processes all tables within the panel to extract structured data.
            tables = panel.find_all("table")
            panel_tables = []

            for table in tables:
                table_info = {}

                # Determines the title of the table, if any, or assigns None if not directly associated.
                h3 = table.find_previous_sibling("h3")
                if h3 and h3 in panel:
                    table_info["title"] = h3.text.strip()
                else:
                    table_info["title"] = None

                # Extracts table headers to use as keys for the data dictionary.
                rows = table.find_all("tr")
                headers = [th.text.strip() for th in rows[0].find_all("th")]

                # Handles tables with more than two columns by creating a list of dictionaries.
                # Each dictionary represents a row in the table.
                if len(headers) > 2:
                    data = []
                    for row in rows[1:]:
                        cols = row.find_all("td")
                        row_data = {}
                        for i in range(len(cols)):
                            header_text = headers[i]
                            cell = cols[i]
                            link = cell.find("a")
                            # If a cell contains a link, it's stored with a key indicating it's a link.
                            if link:
                                row_data[f"{header_text} link"] = link.get("href")
                            row_data[header_text] = cell.text.strip()
                        data.append(row_data)
                else:
                    # For tables with exactly two columns, a dictionary with key-value pairs is created.
                    data = {}
                    for row in rows:
                        cols = row.find_all("td")
                        if len(cols) == 2:
                            data[cols[0].text.strip()] = cols[1].text.strip()

                table_info["data"] = data

                panel_tables.append(table_info)

            # Extracts the Google Maps address if an iframe is present, using regex to clean the URL.
            iframe = panel.find("iframe")
            if iframe:
                panel_info["addressGoogleMaps"] = re.sub(
                    r"\+|%2C",
                    lambda match: " " if match.group(0) == "+" else ", ",
                    re.search(r"q=([^&]+)", iframe.get("src")).group(1),
                )

            # Adds the tables' data to the panel information if any tables were processed.
            if panel_tables:
                panel_info["tables"] = panel_tables

            # Appends the panel's information to the overall information list if it contains any data.
            if panel_info:
                information.append(panel_info)

        # Returns the name and all extracted information from the page.
        return {
            "name": name,
            "information": information,
        }

    def get_provider_detail(self, NPI):
        """
        Retrieves details for a specific provider using their NPI (National Provider Identifier).

        Parameters:
        - NPI (str): National Provider Identifier.

        Returns:
        - A dictionary with the provider's name and additional details extracted from the page.
        """

        return self.__get_page_detail(
            "https://opennpi.com/provider/{NPI}".format(NPI=NPI)
        )

    def get_doctor_detail(self, NPI):
        """
        Retrieves details for a specific doctor using their NPI.

        Parameters:
        - NPI (str): National Provider Identifier.

        Returns:
        - A dictionary with the provider's name and additional details extracted from the page.
        """

        return self.__get_page_detail(
            "https://opennpi.com/physician/{NPI}".format(NPI=NPI)
        )

    def search_providers(
        self, query=None, taxonomy=None, state=None, city=None, zip=None, page=None
    ):
        """
        Performs a search for providers based on various criteria.

        Parameters:
        - query (str): General search term. All parameters are optional and of type str, except `page`.
        - taxonomy (str): Taxonomy code to filter providers by specialty.
        - state (str): State abbreviation to limit the search to a specific geographical location.
        - city (str): City name for the search.
        - zip (str): Postal code for the search.
        - page (int): Page number of results to query.

         Returns:
        - A dictionary with two keys:
          - 'providers': A list of providers matching the search criteria.
          - 'nextPage': A boolean indicating whether more results are available (True if yes, False if no).
        """

        params = {
            "query": query,
            "taxonomy": taxonomy,
            "state": state,
            "city": city,
            "zip": zip,
            "page": page,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.session.get("https://opennpi.com/provider", params=params)
        soup = BeautifulSoup(response.content, "html.parser")

        providers = []
        nextPage = False

        for tr in soup.find("div", {"id": "search-result"}).find_all("tr"):
            if not tr.find("th"):
                if (
                    tr.find("a", "page-link")
                    and tr.find("a", "page-link").text.strip() == "Next Page"
                ):
                    nextPage = True
                    break

                providerName, address, taxonomy, enumerationDate = tr.find_all("td")
                NPI, providerName, address, taxonomy, enumerationDate = (
                    providerName.find("a").get("href").split("/")[-1],
                    providerName.text.strip(),
                    address.text.strip(),
                    taxonomy.text.strip(),
                    enumerationDate.text.strip(),
                )

                providers.append(
                    {
                        "NPI": NPI,
                        "providerName": providerName,
                        "address": address,
                        "taxonomy": taxonomy,
                        "enumerationDate": enumerationDate,
                    }
                )
        return {"providers": providers, "nextPage": nextPage}

    def search_doctors(
        self,
        query=None,
        specialty=None,
        school=None,
        organization=None,
        state=None,
        city=None,
        zip=None,
        page=None,
    ):
        """
        Performs a search for doctors based on various criteria.

        Parameters:
        - query (str): General search term.
        - specialty (str): Medical specialty of the doctor.
        - school (str): Medical school or university of the doctor.
        - organization (str): Organization or medical practice the doctor belongs to.
        - state (str): State abbreviation to limit the search.
        - city (str): City name for the search.
        - zip (str): Postal code for the search.
        - page (int): Page number of results to query. All parameters are optional and of type str, except `page`.

        Returns:
        - A dictionary with two keys:
          - 'doctors': A list of doctors matching the search criteria.
          - 'nextPage': A boolean indicating whether more results are available (True if yes, False if no).
        """

        params = {
            "query": query,
            "specialty": specialty,
            "school": school,
            "organization": organization,
            "state": state,
            "city": city,
            "zip": zip,
            "page": page,
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.session.get("https://opennpi.com/physician", params=params)
        soup = BeautifulSoup(response.content, "html.parser")

        doctors = []
        nextPage = False

        for tr in soup.find("div", {"id": "search-result"}).find_all("tr"):
            if not tr.find("th"):
                if (
                    tr.find("a", "page-link")
                    and tr.find("a", "page-link").text.strip() == "Next Page"
                ):
                    nextPage = True
                    break

                doctorName, primarySpecialty, organizationLegalName, address = (
                    tr.find_all("td")
                )
                (
                    NPI,
                    doctorName,
                    primarySpecialty,
                    organizationLegalName,
                    address,
                ) = (
                    doctorName.find("a").get("href").split("/")[-1],
                    doctorName.text.strip(),
                    primarySpecialty.text.strip(),
                    organizationLegalName.text.strip(),
                    address.text.strip(),
                )

                doctors.append(
                    {
                        "NPI": NPI,
                        "doctorName": doctorName,
                        "primarySpecialty": primarySpecialty,
                        "organizationLegalName": organizationLegalName,
                        "address": address,
                    }
                )
        return {"doctors": doctors, "nextPage": nextPage}
