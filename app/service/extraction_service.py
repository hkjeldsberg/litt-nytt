import defusedxml.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from loguru import logger

from app.config import APP_TIMEOUT


class ExtractionService:
    def __init__(self):
        self.RSS_URL = "https://www.nrk.no/toppsaker.rss"

    @staticmethod
    def fetch_web_page(url):
        response = requests.get(url, timeout=APP_TIMEOUT)
        if response.status_code == 200:
            html = response.text
        else:
            logger.error(f"Failed to retrieve webpage: {url}")
            html = ""

        return html

    def extract_article(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # Parse standard news article
        article_title = soup.find_all("h1", class_="article-title")
        article_text = soup.find_all("div", class_="article-body")

        # Parse bulletin article
        bulletin_article_title = soup.find_all("h2", class_="bulletin-title")
        bulletin_article_text = soup.find_all("div", class_="bulletin-text-body")

        if len(article_text) >= 1 and len(article_title) >= 1:
            text = self.extract_string(article_text)
            title = self.extract_string(article_title)

        elif len(bulletin_article_title) >= 1 and len(bulletin_article_text) >= 1:
            text = self.extract_string(bulletin_article_text)
            title = self.extract_string(bulletin_article_title)
        else:
            logger.warning("Failed to extract article")
            text, title = None, None

        return text, title

    def extract_article_info(self):
        response = requests.get(self.RSS_URL, timeout=APP_TIMEOUT)

        root = ET.fromstring(response.content)
        items = root.findall(".//item")

        # Extract all unique articles
        articles = {}
        for item in items:
            if item.find("link") is not None and "/xl/" not in item.find("link").text:
                article_id = item.find("guid").text
                if article_id not in articles:
                    articles[article_id] = {
                        "url": item.find("link").text,
                        "date": item.find("pubDate").text,
                        "article_id": article_id,
                    }

        return list(articles.values())

    def get_article_info(self):
        logger.info("Extracting article info")
        article_info = self.extract_article_info()

        return article_info

    def get_articles(self, article_info):
        logger.info("Extracting articles")
        for article in article_info:
            html = self.fetch_web_page(article["url"])
            article["text"], article["title"] = self.extract_article(html)

    @staticmethod
    def extract_string(texts):
        text = texts[0].text
        text = text.replace("\n", " ")
        return text
