import pdfplumber


def extract_text(pdf_path):
    """
    Extract all text from the PDF.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_page(pdf_path, page_number):
    """
    Extract text from a single page.
    page_number is zero-based.
    """

    with pdfplumber.open(pdf_path) as pdf:

        if page_number < 0 or page_number >= len(pdf.pages):
            return ""

        page = pdf.pages[page_number]

        text = page.extract_text()

        return text if text else ""