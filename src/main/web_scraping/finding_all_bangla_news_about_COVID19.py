from src.main.data_structure.set_exercise import *
from src.main.web_scraping.scrapper import *
import time

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.106 Chrome/83.0.4103.106 Safari/537.36"
training_keywords = ["করোনা", "কোভিড-১৯", "উহান-ভাইরাস"]  # add keywords here


def find_date_time(string):
    items = string.find_all("time")
    if len(items) > 0:
        for i in items:
            return i.get_text().strip()


def print_only_corona_news(links):
    news_count = 0

    for link in links:
        news_link = get_valid_link(str(link.get("href")))
        title = link.get_text().strip()

        if news_link is None or title is None:
            continue

        title_words = title.split()

        if find_intersection(set(training_keywords), set(title_words)):
            date = find_date_time(scrap_url(news_link, headers))
            logger.info(
                "Published: {}, Heading: {}, Link: {}".format(date, title, news_link)
            )
            news_count += 1
        else:
            metadata = scrap_url(news_link, headers).find_all("meta")
            for tag in metadata:
                if "name" in tag.attrs.keys() and tag.attrs["name"].strip().lower() in [
                    "keywords",
                    "description",
                ]:
                    sample_keywords = tag.attrs["content"].strip().split()

                    if find_intersection(set(training_keywords), set(sample_keywords)):
                        news_count += 1
                        date = find_date_time(scrap_url(news_link, headers))
                        logger.info(
                            "Published: {}, Heading: {}, Link: {}".format(
                                date, title, news_link
                            )
                        )

    return news_count


if __name__ == "__main__":
    begin_time = time.time()
    total_news = 0
    website_list = [
        "https://jamuna.tv",
        "https://bangla.bdnews24.com",
        "https://somoynews.tv",
        "https://prothomalo.com",
    ]  # add target website URL here
    for web_url in website_list:
        soup = scrap_url(web_url, headers)
        all_links = soup.find_all("a")
        total_news += print_only_corona_news(all_links)

    logger.info(
        "Total {} news found within {} seconds.".format(
            total_news, time.time() - begin_time
        )
    )
