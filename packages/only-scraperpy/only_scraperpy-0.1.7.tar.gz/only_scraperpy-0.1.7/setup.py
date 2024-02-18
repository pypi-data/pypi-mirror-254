from setuptools import setup, find_packages

setup(
    name="only_scraperpy",
    version="0.1.7",
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
    package_data={
        "": ["*.dll", "*.dylib", "*.so"],
    },
)
