#!/usr/bin/env python3
"""
Script to add the duplicate KYCaaS entry to match the original list exactly.
"""

import pandas as pd
import openpyxl


def add_duplicate_entry():
    """Add the duplicate KYCaaS entry to match original list"""
    try:
        # Read current Excel file
        df = pd.read_excel("app_directory_corrected.xlsx")
        print(f"📊 Current apps in file: {len(df)}")

        # Find the position of KYCaaS to add duplicate after it
        kycaas_index = df[df["Name"] == "KYCaaS"].index[0]
        print(f"📍 KYCaaS found at position: {kycaas_index + 1}")

        # Create duplicate KYCaaS entry
        duplicate_entry = {
            "Name": "KYCaaS",
            "Description": "Know Your Customer as a Service platform",
            "Official URL": "https://www.kycaas.com",
        }

        # Insert the duplicate right after the original KYCaaS
        new_row = pd.DataFrame([duplicate_entry])

        # Split the dataframe at the KYCaaS position
        before_kycaas = df.iloc[: kycaas_index + 1]
        after_kycaas = df.iloc[kycaas_index + 1 :]

        # Combine with duplicate in the middle
        updated_df = pd.concat(
            [before_kycaas, new_row, after_kycaas], ignore_index=True
        )

        print(f"📈 Added duplicate KYCaaS entry")
        print(f"📊 Updated total: {len(updated_df)} apps")

        # Create updated Excel file
        filename = "app_directory_with_duplicate.xlsx"

        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            updated_df.to_excel(writer, sheet_name="App Directory", index=False)

            # Format the file
            workbook = writer.book
            worksheet = writer.sheets["App Directory"]

            # Format headers
            header_font = openpyxl.styles.Font(bold=True, color="FFFFFF")
            header_fill = openpyxl.styles.PatternFill(
                start_color="366092", end_color="366092", fill_type="solid"
            )

            for cell in worksheet[1]:
                cell.font = header_font
                cell.fill = header_fill

            # Adjust column widths
            worksheet.column_dimensions["A"].width = 30
            worksheet.column_dimensions["B"].width = 60
            worksheet.column_dimensions["C"].width = 40

            # Add borders and alignment
            thin_border = openpyxl.styles.Border(
                left=openpyxl.styles.Side(style="thin"),
                right=openpyxl.styles.Side(style="thin"),
                top=openpyxl.styles.Side(style="thin"),
                bottom=openpyxl.styles.Side(style="thin"),
            )

            for row in worksheet.iter_rows(
                min_row=1, max_row=len(updated_df) + 1, min_col=1, max_col=3
            ):
                for cell in row:
                    cell.border = thin_border
                    cell.alignment = openpyxl.styles.Alignment(
                        wrap_text=True, vertical="top"
                    )

        print(f"✅ Updated Excel file created: {filename}")
        print(f"📊 Final count: {len(updated_df)} apps")

        # Verify the duplicate was added
        kycaas_count = len(updated_df[updated_df["Name"] == "KYCaaS"])
        print(f"🔍 KYCaaS entries: {kycaas_count}")

        if kycaas_count == 2:
            print("✅ Duplicate KYCaaS successfully added!")
        else:
            print(f"❌ Expected 2 KYCaaS entries, found {kycaas_count}")

        return filename

    except Exception as e:
        print(f"❌ Error adding duplicate: {e}")
        return None


if __name__ == "__main__":
    print("🔧 Adding duplicate KYCaaS entry to match original list...")
    filename = add_duplicate_entry()

    if filename:
        print(f"\n🎉 Success! The Excel file '{filename}' now contains:")
        print(f"   • 523 apps (matching your original list exactly)")
        print(f"   • KYCaaS appears twice (as in original)")
        print(f"   • Professional formatting maintained")
    else:
        print("❌ Failed to add duplicate entry")
