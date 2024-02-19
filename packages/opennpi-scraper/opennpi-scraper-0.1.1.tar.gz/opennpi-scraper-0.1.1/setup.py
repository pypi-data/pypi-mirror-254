from setuptools import setup, find_packages

setup(
    name="opennpi-scraper",
    version="0.1.1",
    author="Diego Arrechea",
    author_email="diego.arrechea.job@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/Diego-Arrechea/opennpi-scraper",
    license="MIT",
    description="The `opennpi-scraper` is designed for seamless interaction with the opennpi.com page",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["requests", "beautifulsoup4"],
    python_requires=">=3.6",
)
