from modules.pdf_reader import extract_page

REGIONS = [
    "BestWesterns",
    "BelowBestWesterns",
    "PlainerWesterns",
    "NuwaraEliyas",
    "BrighterUdapussellawas",
    "OtherUdapussellawas",
    "BestUvas",
    "OtherUvas",
    "GoodMediums",
    "OtherMediums",
    "HighGrown",
    "MediumGrown",
    "LowGrown"
]


def extract_quotation(pdf_path, page_number):

    page = extract_page(pdf_path, page_number)

    if not page:
        return []

    start = page.find("QUOTATIONSLKR")
    end = page.find("FORBES&WALKER")

    if start == -1 or end == -1:
        return []

    table = page[start:end]

    lines = table.split("\n")

    data = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        for region in REGIONS:

            if line.startswith(region):

                tokens = line.split()

                data.append({
                    "Region": tokens[0],
                    "BOP_Previous": tokens[1] if len(tokens) > 1 else "",
                    "BOP_Current": tokens[2] if len(tokens) > 2 else "",
                    "BOPF_Previous": tokens[3] if len(tokens) > 3 else "",
                    "BOPF_Current": tokens[4] if len(tokens) > 4 else "",
                    "PEKOE_Previous": tokens[5] if len(tokens) > 5 else "",
                    "PEKOE_Current": tokens[6] if len(tokens) > 6 else "",
                    "OP_Previous": tokens[7] if len(tokens) > 7 else "",
                    "OP_Current": tokens[8] if len(tokens) > 8 else ""
                })

                break

    return data


def extract_high_grown(pdf_path):
    return extract_quotation(pdf_path, 6)


def extract_medium_grown(pdf_path):
    return extract_quotation(pdf_path, 7)


def extract_low_grown(pdf_path):
    return extract_quotation(pdf_path, 9)


def extract_off_grades(pdf_path):
    return extract_quotation(pdf_path, 11)


def extract_dust(pdf_path):
    return extract_quotation(pdf_path, 11)