#!/usr/bin/env python3
"""
Script to fix the Excel file to match the original list exactly.
"""

import pandas as pd
import openpyxl


def fix_excel_file():
    """Remove extra apps and create correct Excel file"""
    try:
        # Read current Excel file
        df = pd.read_excel("app_directory_complete.xlsx")
        print(f"📊 Current apps in file: {len(df)}")

        # Apps that should be removed (not in original list)
        extra_apps = [
            "Airtable",
            "Asana",
            "Docker",
            "Drupal",
            "Joomla",
            "Kubernetes",
            "Notion",
            "PayPal",
            "Shopify",
            "Slack",
            "Stripe",
            "Trello",
            "WordPress",
        ]

        # Remove extra apps
        corrected_df = df[~df["Name"].isin(extra_apps)]
        print(f"📈 Removed {len(extra_apps)} extra apps")
        print(f"📊 Corrected total: {len(corrected_df)} apps")

        # Create corrected Excel file
        filename = "app_directory_corrected.xlsx"

        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            corrected_df.to_excel(writer, sheet_name="App Directory", index=False)

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
                min_row=1, max_row=len(corrected_df) + 1, min_col=1, max_col=3
            ):
                for cell in row:
                    cell.border = thin_border
                    cell.alignment = openpyxl.styles.Alignment(
                        wrap_text=True, vertical="top"
                    )

        print(f"✅ Corrected Excel file created: {filename}")
        print(f"📊 Final count: {len(corrected_df)} apps")

        # Verify no extra apps remain
        remaining_apps = set(corrected_df["Name"].tolist())
        extra_remaining = set(extra_apps) & remaining_apps

        if extra_remaining:
            print(f"⚠️  Still contains extra apps: {extra_remaining}")
        else:
            print("✅ All extra apps removed successfully")

        return filename

    except Exception as e:
        print(f"❌ Error fixing Excel file: {e}")
        return None


if __name__ == "__main__":
    print("🔧 Fixing Excel file to match original list exactly...")
    filename = fix_excel_file()

    if filename:
        print(f"\n🎉 Success! The corrected Excel file '{filename}' now contains:")
        print(f"   • Exactly the apps from your original list")
        print(f"   • No extra apps")
        print(f"   • Professional formatting maintained")
    else:
        print("❌ Failed to fix Excel file")
