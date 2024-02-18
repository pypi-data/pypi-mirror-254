"""Configuration file for the ECB Scraper."""

ROOT_URL = "https://www.ecb.europa.eu"
BASE_INDEX_URL = ROOT_URL + "/press/pressconf/{year}/html/index_include.en.html"
MIN_YEAR = 1998
START_TAG = "Jump to the transcript of the questions and answers"
END_TAG = "\nReproduction is permitted provided that the source is acknowledged"
EXCLUDED_CLASSES = ["title", "address-box", "related-publications", "related-topics", "ecb-pressContentTitle"]


def index_url_year(year):
    """Get the URL for the index page of a given year."""
    return BASE_INDEX_URL.format(year=year)
