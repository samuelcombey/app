#!/usr/bin/env python3
"""
Script to update the Excel file with missing apps from the original list.
"""

import pandas as pd
import openpyxl

# Missing apps that need to be added
missing_apps = [
    {
        "Name": "Slack",
        "Description": "Team communication and collaboration platform",
        "Official URL": "https://slack.com",
    },
    {
        "Name": "Docker",
        "Description": "Containerization platform for application deployment",
        "Official URL": "https://www.docker.com",
    },
    {
        "Name": "Kubernetes",
        "Description": "Container orchestration and management platform",
        "Official URL": "https://kubernetes.io",
    },
    {
        "Name": "Trello",
        "Description": "Project management and task organization platform",
        "Official URL": "https://trello.com",
    },
    {
        "Name": "Asana",
        "Description": "Work management and team collaboration platform",
        "Official URL": "https://asana.com",
    },
    {
        "Name": "Notion",
        "Description": "All-in-one workspace for notes, docs, and collaboration",
        "Official URL": "https://www.notion.so",
    },
    {
        "Name": "Airtable",
        "Description": "Database and spreadsheet hybrid platform",
        "Official URL": "https://airtable.com",
    },
    {
        "Name": "Stripe",
        "Description": "Online payment processing and financial services platform",
        "Official URL": "https://stripe.com",
    },
    {
        "Name": "PayPal",
        "Description": "Digital payment and money transfer platform",
        "Official URL": "https://www.paypal.com",
    },
    {
        "Name": "Shopify",
        "Description": "E-commerce platform for online stores and retail",
        "Official URL": "https://www.shopify.com",
    },
    {
        "Name": "WordPress",
        "Description": "Content management system and website builder",
        "Official URL": "https://wordpress.org",
    },
    {
        "Name": "Drupal",
        "Description": "Open-source content management system",
        "Official URL": "https://www.drupal.org",
    },
    {
        "Name": "Joomla",
        "Description": "Open-source content management system",
        "Official URL": "https://www.joomla.org",
    },
]


def update_excel_file():
    """Update Excel file with missing apps"""
    try:
        # Read existing Excel file
        df = pd.read_excel("app_directory.xlsx")
        print(f"📊 Current apps in file: {len(df)}")

        # Add missing apps
        missing_df = pd.DataFrame(missing_apps)
        updated_df = pd.concat([df, missing_df], ignore_index=True)

        print(f"📈 Adding {len(missing_apps)} missing apps...")
        print(f"📊 Updated total: {len(updated_df)} apps")

        # Create updated Excel file with formatting
        filename = "app_directory_complete.xlsx"

        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            # Write the updated data
            updated_df.to_excel(writer, sheet_name="App Directory", index=False)

            # Get the workbook and worksheet
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
        print(f"📊 Total applications: {len(updated_df)}")

        # Verify the missing apps are now included
        print("\n🔍 Verifying added apps:")
        for app in missing_apps:
            if app["Name"] in updated_df["Name"].values:
                print(f"✅ {app['Name']} - Added successfully")
            else:
                print(f"❌ {app['Name']} - Still missing")

        return filename

    except Exception as e:
        print(f"❌ Error updating Excel file: {e}")
        return None


if __name__ == "__main__":
    print("🔧 Updating Excel file with missing applications...")
    filename = update_excel_file()

    if filename:
        print(
            f"\n🎉 Success! The complete Excel file '{filename}' has been created with:"
        )
        print(f"   • All original apps plus missing ones")
        print(f"   • Professional formatting and styling")
        print(f"   • Ready for immediate use")
    else:
        print("❌ Failed to update Excel file")
