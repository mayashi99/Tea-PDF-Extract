import re

def extract_overall_market(text):

    # Overall Market section එක ගන්න
    pattern = r"Overall Market(.*?)ORDER OF SALE"

    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return []

    section = match.group(1)

    section = re.sub(r"QTY\(M/KGS\)", "", section)
    section = re.sub(r"DEMAND", "", section)

    print(section)     # Debug

    data = []

    # Category  Quantity  Demand
    pattern = r"([A-Za-z&/\-\s]+?)\s+(\d+\.\d+)\s+([A-Za-z]+)"

    rows = re.findall(pattern, section)

    for row in rows:

        data.append({
            "Category": row[0].strip(),
            "Quantity": float(row[1]),
            "Demand": row[2]
        })

    return data