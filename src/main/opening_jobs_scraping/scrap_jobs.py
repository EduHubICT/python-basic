import json
from src.main.web_scraping.scraper import *


def scrap_companies():
    file = open('resource.json')
    data = json.load(file)
    for company in data['companies']:
        name = company['companyName']
        url = company['url']

        if not company['jobs_list'] or not company['jobs_list']['tag']:
            continue

        try:
            tag = company['jobs_list']
            jobs = scrape_url(url)
            jobs = jobs.find_all(tag['tag'], {'class': tag['class'], 'id': tag['id']})
            logger.info("Opening Jobs from {}".format(name))
            for job in jobs:
                content = scrape_content(str(job))
                path = content.find('a').get('href')
                link = get_valid_link(path)
                if not link:
                    link = url + path
                item = content.get_text().strip().split('\n')
                item = [itm.strip() for itm in item]
                print("Job Link: {}".format(link))
                for itm in item:
                    if itm.strip():
                        print(itm.strip())
                if not company['job_info']:
                    continue
                job_info = company['job_info']
                job_details = scrape_url(link)
                job_details = job_details.find_all(job_info['tag'], {'class': job_info['class'], 'id': job_info['id']})
                for info in job_details:
                    details = info.get_text().strip().split('\n')
                    for line in details:
                        if line.strip():
                            print(line.strip())
        except:
            pass


if __name__ == '__main__':
    import time
    curr_time = time.time()
    scrap_companies()
    print("Time spent: {} seconds".format(time.time()-curr_time))
