import logging
import sys
import xml.etree.ElementTree as ET

import requests

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)

from bs4 import BeautifulSoup


class ExtractionService:
    def __init__(self):
        self.RSS_URL = "https://www.nrk.no/toppsaker.rss"

    def extract_article(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
        else:
            logger.error("Failed to retrieve webpage")
            exit()

        soup = BeautifulSoup(html_content, "html.parser")
        article_title = soup.find_all("h1", class_="article-title")
        article = soup.find_all("div", class_="article-body")
        if len(article) >= 1 and len(article_title) >= 1:
            article = article[0].text
            article = article.replace("\n", " ")

            title = article_title[0].text
            title = title.replace("\n", " ")
        else:
            logger.warning("Failed to extract article")
            article, title = None, None

        return article, title

    def extract_urls(self):
        response = requests.get(self.RSS_URL)

        root = ET.fromstring(response.content)
        items = root.findall(".//item")
        urls = [item.iter("link").__next__().text for item in items]

        return urls

    def get_urls(self):
        logger.info("Extracting urls")
        urls = self.extract_urls()

        return urls

    def get_articles(self, urls):
        logger.info("Extracting articles")
        articles = self.extract_article(urls)

        return articles
