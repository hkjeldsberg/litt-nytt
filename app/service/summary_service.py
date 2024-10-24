from loguru import logger
from transformers import BartForConditionalGeneration, BartTokenizer


class SummaryService:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def get_summaries(self, article_info):
        logger.debug("Extracting summaries from articles")
        summaries = [
            {
                "title": article["title"],
                "summary": self.extract_summary(article["text"]),
                "url": article["url"],
                "date": article["date"],
                "id": article["id"],
            }
            for article in article_info
            if article["title"] is not None
        ]

        return summaries

    def extract_summary(self, article):
        inputs = self.tokenizer([article], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(
            inputs["input_ids"], min_length=30, max_length=150, num_beams=2, early_stopping=True
        )
        summary = self.tokenizer.batch_decode(
            summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )[0]

        return summary
