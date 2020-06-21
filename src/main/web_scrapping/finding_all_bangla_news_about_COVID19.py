from src.main.web_scrapping.scrapper import *

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.106 Chrome/83.0.4103.106 Safari/537.36"


def print_only_corona_news(all_link):
    cnt = 0

    for link in all_link:
        title = link.get_text().strip()
        news_link = link.get('href')
        if title.find('করোনা') != -1:
            print('Heading: {}, Link: {}'.format(title, news_link))
            cnt += 1

    return cnt


if __name__ == '__main__':
    tot = 0
    url_list = ["https://prothomalo.com", "https://jamuna.tv", "https://somoynews.tv", "https://bangla.bdnews24.com"]
    for url in url_list:
        soup = scrap_url(url, headers)
        links = soup.find_all('a')
        tot += print_only_corona_news(links)

    print("Total {} news found.".format(tot))
