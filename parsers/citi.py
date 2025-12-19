from parsers.base import BaseParser
from utils.regex import (
    extract_card_last4,
    extract_total_due_generic,
    
)
from utils.citi_overrides import extract_due_date_citi, extract_statement_period_citi, extract_transaction_count_citi
class CITIParser(BaseParser):
    def parse(self, text: str) -> dict:
        return {
            "card_last_4": extract_card_last4(text),
            "statement_period": extract_statement_period_citi(text),
            "total_amount_due": extract_total_due_generic(text),
            "payment_due_date": extract_due_date_citi(text),
            "transaction_count": extract_transaction_count_citi(text),
        }
