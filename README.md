Credit Card Statement Parser
Overview

This project parses credit card PDF statements from multiple Indian banks and extracts key information in a standardized JSON format.
It is designed to handle real-world, messy PDFs using a mix of generic parsing and bank-specific overrides.

Supported Banks

Axis Bank

ICICI Bank

HDFC Bank

IDFC First Bank

Citibank

Data Points Extracted

For each statement, the parser extracts:

Bank Name

Card Last 4 Digits

Statement Period (from → to)

Total Amount Due

Payment Due Date

Transaction Count

Project Structure
credit_card_statement_parser/
├── data/                  # Sample PDF statements
├── detector/              # Bank issuer detection
├── extractor/             # PDF text extraction
├── parsers/               # Bank-specific parsers
├── utils/                 # Regex & bank overrides
├── constants.py
├── main.py
├── requirements.txt
└── README.md

How It Works

PDF Text Extraction
Uses pdfplumber (and pikepdf for locked PDFs) to extract raw text.

Issuer Detection
Identifies the bank based on unique keywords in the statement.

Bank-Specific Parsing
Routes the text to the appropriate bank parser with overrides for edge cases.

Standardized Output
Returns a clean Python dictionary with consistent fields across all banks.

How to Run

Install dependencies:

pip install -r requirements.txt


Run the parser:

python main.py


Update the PDF path in main.py to test different statements.

Sample Output
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

Design Decisions

Rule-based parsing for deterministic fields (dates, amounts).

Bank-specific overrides for layout inconsistencies.

Avoided OCR/ML since statements are digital PDFs.

Focused on correctness and explainability over over-engineering.

Limitations

OCR is not supported (scanned PDFs not handled).

Formats may change if banks redesign statement layouts.

Transaction parsing is count-based, not line-item extraction.

Future Improvements

OCR support for scanned statements

Full transaction table extraction

Schema validation using Pydantic

API wrapper for production use