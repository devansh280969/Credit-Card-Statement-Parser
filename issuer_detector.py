from typing import Optional

ISSUER_KEYWORDS = {
    "HDFC": ["hdfc bank"],
    "ICICI": ["icici bank"],
    "CITI": ["citi", "citi bank"],
    "AXIS": ["axis bank"],
    "IDFC": ["idfc first bank", "idfc bank"]
}

def detect_issuer(text: str) -> Optional[str]:
    text_lower = text.lower()

    for issuer, keywords in ISSUER_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return issuer

    return None
