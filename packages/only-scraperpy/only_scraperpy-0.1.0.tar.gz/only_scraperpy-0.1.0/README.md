# PyOnlyScraper 🚀

## Overview 📖

PyOnlyScraper bridges the gap between Rust and Python, offering a high-performance web scraping tool built upon a compiled version of the [Only Scraper Rust library](https://github.com/edlugora96/only_scraper). This Python adaptation retains the core principles of minimalism and efficiency, making it a superior choice for developers who require the speed of Rust with the flexibility of Python for their scraping tasks. It's designed for those looking to leverage Rust's performance benefits within Python's versatile ecosystem.

## Why PyOnlyScraper? 🤔

In a landscape flooded with web scraping solutions, PyOnlyScraper distinguishes itself by harnessing the raw speed and reliability of Rust, combined with the ease of use and widespread adoption of Python. It eliminates the complexity often associated with performing high-speed scraping tasks in Python, offering a streamlined, Rust-powered backend with a simple Python interface. This unique fusion ensures your scraping operations are both fast and straightforward, without the burden of external dependencies.

## Features 🌟

- **Rust-Powered Performance** ⚡: Built on a compiled Rust library, offering unmatched speed and reliability for web scraping in Python.
- **Zero External Dependencies** 📦: Inherits the simplicity of Only Scraper, requiring only the standard libraries of Rust and Python for operation.
- **Pythonic Interface** 🐍: Provides a seamless and intuitive Python wrapper, making it easy to integrate into any Python project.
- **Focused Functionality** 🔍: Maintains a singular focus on web scraping, without unnecessary features, for optimal efficiency.

## Getting Started 🚀

### Installation 🛠️

To install PyOnlyScraper, use pip to fetch and install the package directly from PyPI:

```bash
pip install only-scraperpy
```

This command will compile the Rust library and install the Python package, making it ready to use in your project.

### Usage 📝

PyOnlyScraper simplifies web scraping in Python by providing a straightforward interface. Here's a quick example to get you started:

```python
from only_scraperpy import OnlyScraper


def main():
    html = OnlyScraper().scrape("https://example.com")
    print(html)


if __name__ == "__main__":
    main()

```

This snippet demonstrates how to fetch and print the HTML content of a specified URL, showcasing the efficiency and ease of use of PyOnlyScraper.

## Original Rust Library

PyOnlyScraper is based on the powerful and efficient [Only Scraper Rust library](https://github.com/edlugora96/only_scraper), created to offer a minimalist and high-performance web scraping solution. For those interested in the Rust version or contributing to its development, please visit the [GitHub repository](https://github.com/edlugora96/only_scraper).

## Contributing 🤝

Contributions are highly appreciated to further refine and enhance PyOnlyScraper. Whether you have ideas for new features, bug fixes, or improvements, we encourage you to share your insights through GitHub issues or pull requests.

## License 📄

PyOnlyScraper is released under the MIT License, embracing the same open-source spirit as its Rust counterpart. For more details, please refer to the LICENSE file in the repository.
