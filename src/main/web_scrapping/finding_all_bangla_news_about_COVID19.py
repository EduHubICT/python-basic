from src.main.web_scrapping.scrapper import *
from src.main.logger.py_logger import *

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.106 Chrome/83.0.4103.106 Safari/537.36"
logger = PyLogger.get_configured_logger()


def find_date_time(string):

    # for somoynews tv
    items = string.find_all('div', {'class': 'news-info'})
    if len(items) > 0:
        for i in items:
            item = scrap_content(i.get_text().strip())
            date = item.find_all('p')
            return str(date[0].get_text().strip().split())

    # for banglanews24.com
    items = string.find_all('p', {'class': 'dateline print-only'})
    if len(items) > 0:
        for i in items:
            item = scrap_content(i.get_text().strip())
            date = item.find_all('p')
            return str(date[0].get_text().strip().split())

    # for jamunanews.tv
    items = string.find_all('time')
    if len(items) > 0:
        for i in items:
            return i.get_text().strip()

    return "sorry, no date found."


def print_only_corona_news(all_link):
    news_count = 0

    for link in all_link:
        title = link.get_text().strip()
        news_link = link.get('href')
        if title.find('করোনা') != -1:
            date = find_date_time(scrap_url(news_link, headers))
            logger.info('Published: {}, Heading: {}, Link: {}'.format(date, title, news_link))
            news_count += 1

    return news_count


if __name__ == '__main__':
    total_news = 0
    url_list = ["https://somoynews.tv", "https://bangla.bdnews24.com"]
    for url in url_list:
        soup = scrap_url(url, headers)
        links = soup.find_all('a')
        total_news += print_only_corona_news(links)

    logger.info("Total {} news found.".format(total_news))
