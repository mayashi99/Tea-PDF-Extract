import re

def extract_settlement_dates(text):

    pattern = (
        r"SETTLEMENTDATES.*?"
        r"(\d{2}/\d{2}/\d{4})\s+"
        r"(\d{2}/\d{2}/\d{4})\s+"
        r"(\d{2}/\d{2}/\d{4})"
    )

    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return []

    return [
        {
            "Payment Type": "10% Payment",
            "Date": match.group(1)
        },
        {
            "Payment Type": "Buyers Prompt",
            "Date": match.group(2)
        },
        {
            "Payment Type": "Sellers Prompt",
            "Date": match.group(3)
        }
    ]