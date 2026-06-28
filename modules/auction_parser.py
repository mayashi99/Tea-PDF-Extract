import re

def extract_auction_details(text):

    # AUCTION DETAILS section එක ගන්න
    pattern = r"AUCTION DETAILS(.*?)FORBES&WALKER"

    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return []

    section = match.group(1)

    # අනවශ්‍ය headers අයින් කරන්න
    remove_words = [
        "LOTS",
        "QUANTITY",
        "SETTLEMENTDATES",
        "10%Payment",
        "BuyersPrompt",
        "SellersPrompt",
        "KGSWEREONOFFER.THEBREAKDOWNISASFOLLOWS:"
    ]

    for word in remove_words:
        section = section.replace(word, "")

    # Category  Lots  Quantity
    pattern = r"([A-Za-z&\-/]+)\s+([\d,]+)\s+([\d,]+)"

    rows = re.findall(pattern, section)

    data = []

    for row in rows:

        data.append({

            "Category": row[0],

            "Lots": int(row[1].replace(",", "")),

            "Quantity": int(row[2].replace(",", ""))

        })

    return data