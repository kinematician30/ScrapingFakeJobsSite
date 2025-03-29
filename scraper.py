import logging
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup as bsp

logging.basicConfig(filename='..\\logs\\bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def make_request_parse(url, hd):
    logger.info('Making Requests')
    try:
        response = requests.get(url, headers=hd)
        if response.status_code == 200:
            logger.info(f'Connected to {url} successfully!')
        else:
            logger.error(f'Could not connect to or receive from {url}')
        web_page = bsp(response.text, 'html.parser')
        return web_page
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(f"Could not proceed! - {e}")
        logger.info(f"Could not proceed! - {e}")
        return None


def extract_from_page(page):
    logger.info('Extracting from web page...')
    jobs = page.find_all('div', class_='card-content')

    all_jobs = []  # temporary

    for job in jobs:
        job_title = job.find('h2', class_='title is-5').text
        company = job.find('h3', class_='subtitle is-6 company').text
        location = job.find('p', class_='location').text.strip().split(',')
        location_city = location[0]
        location_state = location[1].strip()
        date_posted = job.find('time').text
        date_posted = datetime.strptime(date_posted, '%Y-%m-%d')
        date_day = date_posted.strftime('%A')
        date_day_month = date_posted.strftime('%d %B')
        date_year = date_posted.year

        info = {
            "Job_Title": job_title,
            "Company": company,
            "City": location_city,
            "State": location_state,
            "Date_Posted": f"{date_day}, {date_day_month}",
            "Year": date_year
        }
        all_jobs.append(info)
        logger.info(f"Added {info} to temporary storage")
    logger.info("All Jobs Extracted and Transformed")
    return all_jobs


def load_to_file(data, filename="Jobs_Data"):
    logger.info('Loading data...')
    jobs_data = pd.DataFrame(data)
    jobs_data.to_csv(f"{filename}.csv", index=False)
    logger.info('LOADED---Preparing to round up scripts runtime')


def main():
    url = 'https://realpython.github.io/fake-jobs/'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36q (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

    logger.info('Start...')
    wbp = make_request_parse(url=url, hd=header)
    jbd = extract_from_page(page=wbp)
    load_to_file(jbd)

if __name__ == "__main__":
    main()
