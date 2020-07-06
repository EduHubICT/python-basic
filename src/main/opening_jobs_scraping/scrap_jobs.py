import json
from src.main.web_scraping.scrapper import *


def scrap_companies():
    file = open("resource.json")
    data = json.load(file)
    for company in data["companies"]:
        name = company["companyName"]
        url = company["url"]

        try:
            tag = company["find_all"]
            jobs = scrap_url(url)
            jobs = jobs.find_all(tag["tag"], {"class": tag["class"]})
            logger.info("Opening Jobs from {}".format(name))
            for job in jobs:
                content = scrape_content(str(job))
                path = content.find("a").get("href")
                link = get_valid_link(path)
                if not link:
                    link = url + path
                item = content.get_text().strip().split("\n")
                logger.info("Job info: {} \n Job link: \t {}".format(item, link))

        except:
            pass


if __name__ == "__main__":
    scrap_companies()
