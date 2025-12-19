import re

def extract_statement_period_hdfc(text: str):
    from datetime import datetime, timedelta

    # Step 1: extract Statement Date
    m = re.search(r"Statement Date\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    if not m:
        return None

    statement_date = datetime.strptime(m.group(1), "%d/%m/%Y")

    # Step 2: derive billing cycle (~30 days)
    start_date = statement_date - timedelta(days=30)

    return {
        "from": start_date.strftime("%d/%m/%Y"),
        "to": statement_date.strftime("%d/%m/%Y"),
    }
