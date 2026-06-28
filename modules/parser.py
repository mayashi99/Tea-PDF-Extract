import re

def extract_sale_number(text):
    match = re.search(r"SALE\s*NO\s*:?\s*(\d+)", text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None

import re

def extract_report_date(text):

    match = re.search(
        r"\d{2}[A-Z]{2}/\d{2}[A-Z]{2}\s+[A-Z]+\s+\d{4}",
        text
    )

    if match:
        return match.group()

    return None