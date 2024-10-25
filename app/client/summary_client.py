from datetime import datetime

import requests
from loguru import logger

from app.config import HF_TOKEN


class SummaryService:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"

    def get_summaries(self, article_info):
        logger.debug("Extracting summaries from articles")
        summaries = [
            {
                "title": article["title"],
                "summary": self.fetch_summary(article["text"])[0]["summary_text"],
                "url": article["url"],
                "date": self.convert_date_to_iso_format(article["date"]),
                "article_id": article["id"],
            }
            for article in article_info
            if article["title"] is not None
        ]

        return summaries

    def fetch_summary(self, article):
        body = {
            "inputs": article,
            "parameters": {"min_length": 30, "max_length": 120, "clean_up_tokenization_spaces": True},
        }
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        try:
            response = requests.post(self.API_URL, headers=headers, json=body)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        return {}

    @staticmethod
    def convert_date_to_iso_format(date):
        parsed_date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
        iso_format = parsed_date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        return iso_format
