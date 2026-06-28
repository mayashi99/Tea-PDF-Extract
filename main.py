from pathlib import Path

from modules.pdf_reader import extract_text
from modules.parser import extract_sale_number, extract_report_date
from modules.overall_market_parser import extract_overall_market
from modules.auction_parser import extract_auction_details
from modules.settlement_parser import extract_settlement_dates
from modules.excel_writer import save_to_excel

from modules.quotation_parser import (
    extract_high_grown,
    extract_medium_grown,
    extract_low_grown,
    extract_off_grades,
    extract_dust
)

# ==========================================
# INPUT PDF FOLDER
# ==========================================

pdf_folder = Path("input_pdfs")
pdf_files = list(pdf_folder.glob("*.pdf"))

# ==========================================
# MASTER LISTS
# ==========================================

all_summary = []
all_overall = []
all_auction = []
all_settlement = []
all_high = []
all_medium = []
all_low = []
all_off = []
all_dust = []

# ==========================================
# PROCESS EACH PDF
# ==========================================

for pdf_path in pdf_files:

    print("\n" + "=" * 80)
    print("PROCESSING :", pdf_path.name)
    print("=" * 80)

    text = extract_text(pdf_path)

    sale_no = extract_sale_number(text)
    report_date = extract_report_date(text)

    summary = [{
        "Sale No": sale_no,
        "Report Date": report_date
    }]

    overall = extract_overall_market(text)
    auction = extract_auction_details(text)
    settlement = extract_settlement_dates(text)

    high = extract_high_grown(pdf_path)
    medium = extract_medium_grown(pdf_path)
    low = extract_low_grown(pdf_path)
    off = extract_off_grades(pdf_path)
    dust = extract_dust(pdf_path)

    print("Summary :", len(summary))
    print("Overall :", len(overall))
    print("Auction :", len(auction))
    print("Settlement :", len(settlement))
    print("High :", len(high))
    print("Medium :", len(medium))
    print("Low :", len(low))
    print("Off :", len(off))
    print("Dust :", len(dust))

    all_summary.extend(summary)
    all_overall.extend(overall)
    all_auction.extend(auction)
    all_settlement.extend(settlement)
    all_high.extend(high)
    all_medium.extend(medium)
    all_low.extend(low)
    all_off.extend(off)
    all_dust.extend(dust)

# ==========================================
# SAVE TO EXCEL
# ==========================================

save_to_excel(
    all_summary,
    all_overall,
    all_auction,
    all_settlement,
    all_high,
    all_medium,
    all_low,
    all_off,
    all_dust
)

print("\nTea_Report.xlsx created successfully!")