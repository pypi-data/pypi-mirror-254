from setuptools import setup, find_packages

setup(
    name="only_scraperpy",
    version="0.1.2",
    packages=find_packages(),
    license="MIT",
    description="Only scrape webpages from rust to python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Eduardo Gonzalez",
    author_email="me@edlugora.com",
    url="https://github.com/edlugora96/only_scraperpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
        (
            "bin",
            [
                "only_scraperpy/only_scraper.so",
                "only_scraperpy/only_scraper.dll",
                "only_scraperpy/only_scraper.dylib",
                "only_scraperpy/only_scraper.rlib",
            ],
        )
    ],
)
