from parsers.base import BaseParser
from utils.regex import (
    extract_due_date,
    extract_total_due_icici,
    extract_statement_period,
    extract_transaction_count,
    
)
#from utils.regex import extract_total_due_icici  # your working function
from utils.icici_overrides import extract_card_last4_icici
class ICICIParser(BaseParser):
    def parse(self, text: str) -> dict:
        return {
            "card_last_4": extract_card_last4_icici(text),
            "statement_period": extract_statement_period(text),
            "total_amount_due": extract_total_due_icici(text),
            "payment_due_date": extract_due_date(text),
            "transaction_count": extract_transaction_count(text),
        }
