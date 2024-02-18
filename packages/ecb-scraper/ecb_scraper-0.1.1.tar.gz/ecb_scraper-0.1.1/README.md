<h1 align="center">ECB Scraper</h1>

<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/ecb-scraper">
    <br>
    <a href="https://pypi.org/project/ecb-scraper/"><img src="https://badge.fury.io/py/ecb-scraper.svg" alt="PyPI version"></a>
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

ECB Scraper is a Python package for scraping European Central Bank press conference transcripts. It allows for easy extraction of press conference details including dates and URLs, offering a streamlined way to access ECB statements and Q&A sessions over the years.

## Installation

Install `ecb-scraper` via pip:

```bash
pip install ecb-scraper
```

## Usage

### CLI

The ECB Scraper also provides a Command Line Interface (CLI) for fetching ECB press conferences without needing to write any Python code. Here's how you can use it:

Arguments
- --start-year: Specify the start year for fetching the conferences. If not provided, the script will use 1998.
- --end-year: Specify the end year for fetching the conferences. If not provided, the current year is used.
- --output-file: Required. The path to the file where the fetched data will be saved (CSV or JSON).

```bash
ecb-scraper --start-year 2019 --end-year 2020 --output-file conferences.json
```

### Python

The ECB Scraper can also be used as a Python package. Here's how you can use it:

```python
from ecb_scraper import get_all_conferences

# DataFrame with columns ['date', 'title', 'link', 'text']
conferences = get_all_conferences(start_year=2005, end_year=2020)
```
