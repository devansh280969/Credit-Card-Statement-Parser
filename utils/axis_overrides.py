import re

def extract_due_date_axis(text: str):
    """
    FINAL AXIS LOGIC:
    - Find 'Payment Summary' header row
    - Read the next line (values)
    - Extract all DD/MM/YYYY dates
    - Return the SECOND LAST date (Payment Due Date)
    """

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    for i, line in enumerate(lines):
        if (
            "payment summary" in line.lower()
            or (
                "payment due date" in line.lower()
                and "statement period" in line.lower()
            )
        ):
            if i + 1 < len(lines):
                values_line = lines[i + 1]

                dates = re.findall(
                    r"\d{2}/\d{2}/\d{4}",
                    values_line
                )

                # AXIS pattern:
                # [statement_start, statement_end, payment_due_date, generation_date]
                if len(dates) >= 3:
                    return dates[-2]  # ← THIS IS THE FIX

    return None

