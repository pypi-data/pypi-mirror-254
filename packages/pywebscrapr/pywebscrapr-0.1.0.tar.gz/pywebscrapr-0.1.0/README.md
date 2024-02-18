# PyWebScrapr
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Code Size](https://img.shields.io/github/languages/code-size/Infinitode/PyWebScrapr)
![Downloads](https://pepy.tech/badge/pywebscapr)
![License Compliance](https://img.shields.io/badge/license-compliance-brightgreen.svg)
![PyPI Version](https://img.shields.io/pypi/v/pywebscrapr)

An open-source Python library for web scraping tasks. Includes support for both text and image scraping.

## Installation

You can install PyWebScrapr using pip:

```bash
pip install pywebscrapr
```

## Supported Python Versions

PyWebScrapr supports the following Python versions:

- Python 3.6
- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11/Later (Preferred)

Please ensure that you have one of these Python versions installed before using PyWebScrapr. PyWebScrapr may not work as expected on lower versions of Python than the supported.

## Features

- **Text Scraping**: Extract textual content from specified URLs.
- **Image Scraping**: Download images from specified URLs.

<sub>*for a full list check out the PyWebScrapr Documentation.</sub>

## Usage

### Text Scraping

```python
from pywebscrapr import scrape_text

# Specify links in a file or list
links_file = 'links.txt'
links_array = ['https://example.com/page1', 'https://example.com/page2']

# Scrape text and save to the 'output.txt' file
scrape_text(links_file=links_file, links_array=links_array, output_file='output.txt')
```

### Image Scraping

```python
from pywebscrapr import scrape_images

# Specify links in a file or list
links_file = 'image_links.txt'
links_array = ['https://example.com/image1.jpg', 'https://example.com/image2.png']

# Scrape images and save to the 'images' folder
scrape_images(links_file=links_file, links_array=links_array, save_folder='images')
```

## Contributing

Contributions are welcome! If you encounter any issues, have suggestions, or want to contribute to PyWebScrapr, please open an issue or submit a pull request on [GitHub](https://github.com/infinitode/pywebscrapr).

## License

PyWebScrapr is released under the terms of the **MIT License (Modified)**. Please see the [LICENSE](https://github.com/infinitode/pywebscrapr/blob/main/LICENSE) file for the full text.

**Modified License Clause**

The modified license clause grants users the permission to make derivative works based on the PyWebScrapr software. However, it requires any substantial changes to the software to be clearly distinguished from the original work and distributed under a different name.
