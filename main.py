from pdf_extractor import extract_text
from issuer_detector import detect_issuer
from parsers.router import get_parser


def run(pdf_path: str):
    text = extract_text(pdf_path)

    issuer = detect_issuer(text)
    parser = get_parser(issuer)

    parsed_data = parser.parse(text)

    result = {
        "bank_name": issuer,
        **parsed_data
    }

    return result


if __name__ == "__main__":
    pdf_path = "data/Axis_1.pdf"   # change path to test other PDFs
    output = run(pdf_path)
    print(output)
