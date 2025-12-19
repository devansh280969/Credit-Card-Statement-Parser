import re
from typing import Optional
from constants import TOTAL_DUE_KEYWORDS


def extract_card_last4(text: str):
    

    # 1️⃣ Look for explicit "Card" lines first (most reliable)
    for line in text.splitlines():
        l = line.lower()
        if "card" in l and any(x in l for x in ["xxxx", "xx", "***", "*"]):
            match = re.search(r"(\d{4})\s*$", line)
            if match:
                return match.group(1)

    # 2️⃣ Fallback: masked card number anywhere, take LAST 4 digits only
    matches = re.findall(
        r"(?:xxxx|xx|\*{2,})[\s\-]*\d*[\s\-]*(\d{4})(?!\d)",
        text,
        re.IGNORECASE
    )

    if matches:
        return matches[-1]  # ALWAYS take the last occurrence

    return None






def extract_total_due_generic(text: str):
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    for i, line in enumerate(lines):
        low = line.lower()

        if any(keyword in low for keyword in TOTAL_DUE_KEYWORDS):
            search_block = " ".join(lines[i:i+4])

            amounts = re.findall(r"([\d,]+\.\d{2})", search_block)

            for amt in amounts:
                value = float(amt.replace(",", ""))
                if value > 0:          # 🔑 THIS IS THE FIX
                    return value

    return None






def extract_due_date(text: str):
    

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    for i, line in enumerate(lines):
        if "due date" in line.lower():
            # Look at next few lines for a date
            search_window = " ".join(lines[i:i+4])

            # Numeric dates (DD/MM/YYYY or DD/MM/YY)
            m1 = re.search(r"\d{2}[\/\-]\d{2}[\/\-]\d{2,4}", search_window)
            if m1:
                return m1.group(0)

            # Month name dates (11 Oct 2022)
            m2 = re.search(
                r"\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4}",
                search_window
            )
            if m2:
                return m2.group(0)

    return None






def extract_statement_period(text: str):
    

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    for line in lines:
        # Pattern: DD/MM/YYYY - DD/MM/YYYY
        m = re.search(
            r"(\d{2}/\d{2}/\d{4})\s*[-to]+\s*(\d{2}/\d{2}/\d{4})",
            line,
            re.IGNORECASE
        )
        if m:
            return {
                "from": m.group(1),
                "to": m.group(2),
            }

    return None




def extract_transaction_count(text: str) -> int:
    """
    Count number of transactions by counting date-starting lines.
    """
   

    count = 0
    for line in text.splitlines():
        if re.match(r"\d{2}/\d{2}/\d{4}", line.strip()):
            count += 1

    return count











def extract_total_due_icici(text: str) -> Optional[float]:
    """
    Specifically handles the ICICI side-by-side layout by 
    identifying the labels and grabbing the correct subsequent value.
    """
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        # Look for the line containing both headers
        if "minimum amount due" in line.lower() and "total amount due" in line.lower():
            # Create a search block of the next few lines
            # In your text, the values are on lines i+1 and i+2
            search_block = " ".join(lines[i+1 : i+4]).replace('|', ' ')
            
            # Find ALL currency amounts in this block
            amounts = re.findall(r"[\d,]+\.\d{2}", search_block)
            
            # POSITIONAL RULE:
            # Index 0 is Minimum Due (6,790.00)
            # Index 1 is Total Due (25,887.20)
            if len(amounts) >= 2:
                total_due_str = amounts[1].replace(",", "")
                return float(total_due_str)
                
    return None