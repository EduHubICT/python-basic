from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.parse import urlparse
from src.main.logger.py_logger import PyLogger
import requests
import re


logger = PyLogger.get_configured_logger()


def scrape_content(content):
    return BeautifulSoup(
        BeautifulSoup(content, "html.parser").prettify(), "html.parser"
    )


def get_valid_link(url):
    parse_url = urlparse(url, "http")
    if parse_url.path is not None:
        url = parse_url.geturl()
        regex = re.compile(
            r"^(?:http|ftp)s?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )
        if re.match(regex, url):
            return url


def scrap_url(url, headers=None):
    try:
        page = requests.get(url, headers)
        page.raise_for_status()
    except HTTPError as e:
        logger.info(f"{e}")
    except Exception as err:
        logger.info(f"{err}")
    else:
        soup = BeautifulSoup(page.content, "html.parser")
        soup = BeautifulSoup(soup.prettify(), "html.parser")
        return soup

    return BeautifulSoup("<html></html>", "html.parser")  # return empty result
