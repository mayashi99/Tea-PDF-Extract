from pathlib import Path

import pandas as pd


def save_to_excel(
    summary,
    overall,
    auction,
    settlement,
    high,
    medium,
    low,
    off,
    dust,
    output_path="output/Tea_Report.xlsx"
):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        # Summary
        summary_df = pd.DataFrame(summary)
        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

        # Overall Market
        overall_df = pd.DataFrame(overall)
        overall_df.to_excel(
            writer,
            sheet_name="Overall_Market",
            index=False
        )

        # Auction Details
        auction_df = pd.DataFrame(auction)
        auction_df.to_excel(
            writer,
            sheet_name="Auction_Details",
            index=False
        )

        # Settlement Dates
        pd.DataFrame(settlement).to_excel(
            writer,
            sheet_name="Settlement_Dates",
            index=False
        )
        # High Grown
        high_df = pd.DataFrame(high)
        high_df.to_excel(
            writer,
            sheet_name="High_Grown",
            index=False
        )

        # Medium Grown
        medium_df = pd.DataFrame(medium)
        medium_df.to_excel(
            writer,
            sheet_name="Medium_Grown",
            index=False
        )
        # Low Grown
        low_df = pd.DataFrame(low)
        low_df.to_excel(
           writer,
           sheet_name="Low_Grown",
           index=False
        )
        # Off Grades
        off_df = pd.DataFrame(off)

        off_df.to_excel(
           writer,
           sheet_name="Off_Grades",
           index=False
       )
        #Dust
        dust_df = pd.DataFrame(dust)

        dust_df.to_excel(
           writer,
           sheet_name="Dust",
           index=False
       )

    print(f"{output_file} created successfully!")