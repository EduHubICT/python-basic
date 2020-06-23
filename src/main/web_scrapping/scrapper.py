from bs4 import BeautifulSoup
import requests


def scrap_content(string):
    return BeautifulSoup(BeautifulSoup(string).prettify())


def scrap_url(url, headers=None):

    page = requests.get(url, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(soup.prettify(), 'html.parser')
    return soup
