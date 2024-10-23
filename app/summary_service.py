import logging
import sys

from transformers import BartForConditionalGeneration, BartTokenizer

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class SummaryService:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def get_summaries(self, articles):
        logger.info("Extracting summaries from articles")
        summaries = []
        for article in articles:
            summary = self.extract_summaries(article)
            summaries.append(summary)

        return summaries

    def extract_summaries(self, article):
        inputs = self.tokenizer(
            [article],
            max_length=1024,
            return_tensors="pt",
            truncation=True
        )
        summary_ids = self.model.generate(
            inputs["input_ids"],
            min_length=30,
            max_length=150,
            num_beams=2,
            early_stopping=True
        )
        summary = self.tokenizer.batch_decode(
            summary_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )[0]

        return summary
