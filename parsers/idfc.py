from parsers.base import BaseParser
from utils.regex import (
    extract_card_last4,
    extract_due_date,
    extract_total_due_generic,
    extract_statement_period,
    extract_transaction_count,
    
)
class IDFCParser(BaseParser):
    def parse(self, text: str) -> dict:
        return {
            "card_last_4": extract_card_last4(text),
            "statement_period": extract_statement_period(text),
            "total_amount_due": extract_total_due_generic(text),
            "payment_due_date": extract_due_date(text),
            "transaction_count": extract_transaction_count(text),
        }
