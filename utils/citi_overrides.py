# utils/citi_overrides.py

import re


def extract_due_date_citi(text: str):
    """
    FINAL CITI RULE (guaranteed for this PDF):
    - Extract ALL DD/MM/YY or DD/MM/YYYY dates
    - First date  = Statement Date
    - Second date = Payment Due Date
    """

    dates = re.findall(
        r"\b\d{2}/\d{2}/\d{2,4}\b",
        text
    )

    if len(dates) >= 2:
        return dates[1]

    return None


def extract_statement_period_citi(text: str):

    m = re.search(
        r"Statement Period:\s*(\d{1,2}\s+\w+\s+\d{4})\s+to\s+(\d{1,2}\s+\w+\s+\d{4})",
        text,
        re.IGNORECASE
    )

    if m:
        return {
            "from": m.group(1),
            "to": m.group(2),
        }

    return None



def extract_transaction_count_citi(text: str) -> int:
    import re

    count = 0

    for line in text.splitlines():
        line = line.strip()

        # Match ONLY real Citi transaction rows
        # Format:
        # DD/MM <digits> <text> <amount>
        if re.match(
            r"^\d{2}/\d{2}\s+\d+\s+.+\s+[\d,]+\.\d{2}(CR)?$",
            line
        ):
            count += 1

    return count
