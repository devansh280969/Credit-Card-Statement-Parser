import re

def extract_card_last4_icici(text: str):
    import re
    match = re.search(r"XXXX\s+XXXX\s+(\d{3,4})", text)
    return match.group(1) if match else None
