# Credit Card Statement Parser

## Overview
This project is a **Python-based PDF parser** that extracts key information from **credit card statements** issued by multiple banks.  
It is designed to handle **real-world statement formats**, which often vary across banks and contain inconsistent layouts.

The parser outputs a **standardized JSON structure**, regardless of the bank.

---

## Supported Banks
- Axis Bank  
- ICICI Bank  
- HDFC Bank  
- IDFC First Bank  
- Citibank  

---

## Extracted Data Points
For each credit card statement, the parser extracts:

- **Bank Name**
- **Card Last 4 Digits**
- **Statement Period** (From → To)
- **Total Amount Due**
- **Payment Due Date**
- **Transaction Count**

---

## Project Structure

```markdown
credit-card-statement-parser/
├── data/               # Sample credit card PDFs
├── detector/           # Bank issuer detection
├── extractor/          # PDF text extraction logic
├── parsers/            # Bank-specific parsers
├── utils/              # Regex helpers & bank overrides
├── constants.py        # Global constants
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## How It Works

### 1. PDF Text Extraction
- Uses **pdfplumber** to extract text from digital PDFs.
- Uses **pikepdf** to handle password-protected statements.

### 2. Bank Detection
- Identifies the issuing bank using unique keywords present in the statement text.

### 3. Parsing Logic
- Routes the extracted text to the appropriate **bank-specific parser**.
- Uses **generic parsing rules** where possible.
- Applies **bank-specific overrides** to handle layout inconsistencies.

### 4. Standardized Output
- Produces a consistent output structure for all supported banks.

---

## How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
python main.py
```

### Sample Output
```json
{
  "bank_name": "AXIS",
  "card_last_4": "7381",
  "statement_period": {
    "from": "17/09/2021",
    "to": "15/10/2021"
  },
  "total_amount_due": 78708.38,
  "payment_due_date": "04/11/2021",
  "transaction_count": 54
}
```

## Design Decisions
- **Rule-based parsing** was chosen for deterministic fields (dates, amounts, card numbers) to ensure accuracy, transparency, and debuggability.
- A **modular parser architecture** was implemented, with a base parser and bank-specific overrides, to cleanly handle layout differences across issuers.
- **Bank detection is performed upfront**, allowing automatic routing of statements to the correct parser without manual configuration.
- **Generic logic is reused wherever possible**, with overrides added only when a bank’s format deviates significantly (e.g., Citi transaction dates).
- OCR and AI/LLM approaches were **intentionally avoided** because the statements are digital PDFs; deterministic parsing is more reliable and auditable.
- The system prioritizes **correctness and maintainability** over over-engineering, making it easy to extend support for additional banks in the future.

## Limitations
- **OCR is not supported**; the parser does not handle scanned or image-only PDF statements.
- Statement parsing may break if banks **significantly redesign their statement layouts**.
- Transaction extraction is **count-based only** and does not return detailed line-item transaction data.
- The parser assumes **English-language statements** and may not work correctly for other languages.
- Password-protected PDFs are supported only when the correct password is provided.

## Future Improvements
- Add OCR support (e.g., Tesseract) to handle scanned or image-based PDF statements.
- Extract full transaction tables with structured line-item data instead of only transaction counts.
- Introduce schema validation using Pydantic to enforce consistent and type-safe outputs.
- Add an optional AI/LLM-based fallback for highly irregular or previously unseen statement formats.
- Expose the parser through a REST API (e.g., FastAPI) for easier integration into other systems.
- Improve error handling and logging for better observability in production environments.


