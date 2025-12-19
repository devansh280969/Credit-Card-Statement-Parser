import pdfplumber
import pikepdf
import os


def extract_text(pdf_path: str, password: str | None = None) -> str:
    """
    Extract raw text from a PDF.
    Handles password-protected PDFs.
    Returns extracted text (can be empty).
    """

    temp_path = pdf_path

    # Step 1: Decrypt if password is provided
    if password:
        try:
            with pikepdf.open(pdf_path, password=password) as pdf:
                temp_path = "temp_unlocked.pdf"
                pdf.save(temp_path)
        except Exception as e:
            print(f"[ERROR] Failed to decrypt PDF: {e}")
            return ""

    # Step 2: Extract text using pdfplumber
    text = ""
    try:
        with pdfplumber.open(temp_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text() or ""
                text += f"\n--- PAGE {page_num} ---\n"
                text += page_text
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")

    # Cleanup temp file
    if temp_path != pdf_path and os.path.exists(temp_path):
        os.remove(temp_path)

    return text.strip()
