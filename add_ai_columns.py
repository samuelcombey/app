#!/usr/bin/env python3
"""
Script to add AI-related columns to the Excel file.
"""

import pandas as pd
import openpyxl


def add_ai_columns():
    """Add AI-related columns to the Excel file"""
    try:
        # Read current Excel file
        df = pd.read_excel("app_directory_with_duplicate.xlsx")
        print(f"📊 Current apps in file: {len(df)}")

        # Add new AI columns with default values
        df["lxAiPotential"] = "unknown"  # Default value for all apps
        df["lxAiRisk"] = "unknown"  # Default value for all apps
        df["lxAiUsage"] = "unknown"  # Default value for all apps
        df["lxAiType"] = "unknown"  # Default value for all apps
        df["lxAiTaxonomyDescription"] = ""  # Empty string for all apps

        print(f"📈 Added 5 AI-related columns:")
        print(f"   • lxAiPotential: String (low, medium, high, veryHigh)")
        print(f"   • lxAiRisk: String (minimal, limited, high, unacceptable)")
        print(f"   • lxAiUsage: String (unknown, noAiUsage, aiAvailable, aiEnabled)")
        print(f"   • lxAiType: String (neuralNet, llm, machineLearning, Other)")
        print(f"   • lxAiTaxonomyDescription: String")

        # Create updated Excel file
        filename = "app_directory_with_ai_columns.xlsx"

        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="App Directory", index=False)

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
            worksheet.column_dimensions["A"].width = 30  # Name
            worksheet.column_dimensions["B"].width = 60  # Description
            worksheet.column_dimensions["C"].width = 40  # Official URL
            worksheet.column_dimensions["D"].width = 15  # lxAiPotential
            worksheet.column_dimensions["E"].width = 15  # lxAiRisk
            worksheet.column_dimensions["F"].width = 15  # lxAiUsage
            worksheet.column_dimensions["G"].width = 20  # lxAiType
            worksheet.column_dimensions["H"].width = 40  # lxAiTaxonomyDescription

            # Add borders and alignment
            thin_border = openpyxl.styles.Border(
                left=openpyxl.styles.Side(style="thin"),
                right=openpyxl.styles.Side(style="thin"),
                top=openpyxl.styles.Side(style="thin"),
                bottom=openpyxl.styles.Side(style="thin"),
            )

            for row in worksheet.iter_rows(
                min_row=1, max_row=len(df) + 1, min_col=1, max_col=8
            ):
                for cell in row:
                    cell.border = thin_border
                    cell.alignment = openpyxl.styles.Alignment(
                        wrap_text=True, vertical="top"
                    )

        print(f"✅ Updated Excel file created: {filename}")
        print(f"📊 Total columns: {len(df.columns)}")
        print(f"📊 Total rows: {len(df)}")

        # Show column names
        print(f"\n📋 Column names:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i}. {col}")

        # Show sample data
        print(f"\n📋 Sample data (first 3 rows):")
        sample_cols = ["Name", "lxAiPotential", "lxAiRisk", "lxAiUsage", "lxAiType"]
        print(df[sample_cols].head(3).to_string(index=False))

        return filename

    except Exception as e:
        print(f"❌ Error adding AI columns: {e}")
        return None


if __name__ == "__main__":
    print("🔧 Adding AI-related columns to Excel file...")
    filename = add_ai_columns()

    if filename:
        print(f"\n🎉 Success! The Excel file '{filename}' now contains:")
        print(f"   • All original columns (Name, Description, Official URL)")
        print(f"   • 5 new AI-related columns with default values")
        print(f"   • Professional formatting maintained")
        print(f"   • Ready for AI data entry")
    else:
        print("❌ Failed to add AI columns")
