#!/usr/bin/env python3
"""
Update the main Excel file with proper AI research results using 8-step methodology
"""

import pandas as pd
import openpyxl
from datetime import datetime


def update_main_excel_with_proper_research():
    """Update the main Excel file with proper AI research results"""

    print("🔄 UPDATING MAIN EXCEL WITH PROPER AI RESEARCH")
    print("=" * 60)

    # Read the proper research results
    research_df = pd.read_excel(
        "proper_ai_research_results.xlsx", sheet_name="Research Results"
    )

    # Read the main Excel file
    main_df = pd.read_excel("app_directory_with_ai_data.xlsx")

    print(f"📊 Main file: {len(main_df)} apps")
    print(f"📊 Research results: {len(research_df)} apps")

    # Create a mapping from research results
    research_mapping = {}
    for _, row in research_df.iterrows():
        app_name = row["App Name"]
        research_mapping[app_name] = {
            "lxAiPotential": row["AI Potential"],
            "lxAiRisk": row["AI Risk"],
            "lxAiUsage": row["AI Usage"],
            "lxAiType": row["AI Type"],
            "lxAiTaxonomyDescription": row["AI Taxonomy Description"],
        }

    # Update the main DataFrame with research results
    updated_count = 0
    for index, row in main_df.iterrows():
        app_name = row["Name"]
        if app_name in research_mapping:
            # Update AI columns with research results
            main_df.at[index, "lxAiPotential"] = research_mapping[app_name][
                "lxAiPotential"
            ]
            main_df.at[index, "lxAiRisk"] = research_mapping[app_name]["lxAiRisk"]
            main_df.at[index, "lxAiUsage"] = research_mapping[app_name]["lxAiUsage"]
            main_df.at[index, "lxAiType"] = research_mapping[app_name]["lxAiType"]
            main_df.at[index, "lxAiTaxonomyDescription"] = research_mapping[app_name][
                "lxAiTaxonomyDescription"
            ]
            updated_count += 1

    print(f"✅ Updated {updated_count} apps with proper research results")

    # Create the final Excel file
    filename = "app_directory_final_proper_ai_research.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main updated sheet
        main_df.to_excel(writer, sheet_name="App Directory", index=False)

        # AI Research Summary
        summary_data = {
            "Metric": [
                "Total Apps",
                "AI-Enabled Apps",
                "AI-Available Apps",
                "No AI Usage",
                "High/Very High Potential",
                "High Risk Apps",
                "LLM Technology",
                "Machine Learning",
                "Neural Networks",
                "High Confidence Results",
                "Medium Confidence Results",
                "Low Confidence Results",
                "Updated with Research",
            ],
            "Count": [
                len(main_df),
                len(main_df[main_df["lxAiUsage"] == "aiEnabled"]),
                len(main_df[main_df["lxAiUsage"] == "aiAvailable"]),
                len(main_df[main_df["lxAiUsage"] == "noAiUsage"]),
                len(main_df[main_df["lxAiPotential"].isin(["high", "veryHigh"])]),
                len(main_df[main_df["lxAiRisk"] == "high"]),
                len(main_df[main_df["lxAiType"] == "llm"]),
                len(main_df[main_df["lxAiType"] == "machineLearning"]),
                len(main_df[main_df["lxAiType"] == "neuralNet"]),
                len(research_df[research_df["Confidence Level"] == "high"]),
                len(research_df[research_df["Confidence Level"] == "medium"]),
                len(research_df[research_df["Confidence Level"] == "low"]),
                updated_count,
            ],
        }

        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name="AI Research Summary", index=False)

        # High Confidence Results
        high_confidence = research_df[research_df["Confidence Level"] == "high"]
        high_confidence.to_excel(
            writer, sheet_name="High Confidence Results", index=False
        )

        # AI-Enabled Apps
        ai_enabled = main_df[main_df["lxAiUsage"] == "aiEnabled"]
        ai_enabled.to_excel(writer, sheet_name="AI-Enabled Apps", index=False)

        # High Potential Apps
        high_potential = main_df[main_df["lxAiPotential"].isin(["high", "veryHigh"])]
        high_potential.to_excel(writer, sheet_name="High Potential Apps", index=False)

        # AI-Available Apps
        ai_available = main_df[main_df["lxAiUsage"] == "aiAvailable"]
        ai_available.to_excel(writer, sheet_name="AI-Available Apps", index=False)

        # Research Methodology
        methodology_data = {
            "Research Step": [
                "1. Visit Official Website",
                "2. Check Product Documentation",
                "3. Review Feature Lists",
                "4. Search Recent News",
                "5. Check AI Partnerships",
                "6. Review User Feedback",
                "7. Verify Technical Details",
                "8. Document Findings",
            ],
            "What to Look For": [
                "AI/ML product pages, features, capabilities",
                "Technical specifications, AI documentation",
                "AI-powered features, automation capabilities",
                "AI announcements, new features, partnerships",
                "AI vendor relationships, integrations",
                "User reviews mentioning AI features",
                "API documentation, developer resources",
                "Clear classification with sources",
            ],
            "Time Estimate": [
                "5-10 minutes",
                "10-15 minutes",
                "5-10 minutes",
                "5-10 minutes",
                "5-10 minutes",
                "10-15 minutes",
                "10-20 minutes",
                "5-10 minutes",
            ],
        }

        methodology_df = pd.DataFrame(methodology_data)
        methodology_df.to_excel(writer, sheet_name="Research Methodology", index=False)

        # Format the workbook
        workbook = writer.book

        # Format headers for all sheets
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]

            # Header formatting
            header_font = openpyxl.styles.Font(bold=True, color="FFFFFF")
            header_fill = openpyxl.styles.PatternFill(
                start_color="366092", end_color="366092", fill_type="solid"
            )

            for cell in worksheet[1]:
                cell.font = header_font
                cell.fill = header_fill

            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column_letter].width = adjusted_width

    print(f"\n📋 Final Excel file created: {filename}")

    # Show final summary
    print(f"\n📊 FINAL SUMMARY:")
    print(f"   • Total apps: {len(main_df)}")
    print(f"   • AI-enabled: {len(main_df[main_df['lxAiUsage'] == 'aiEnabled'])}")
    print(f"   • AI-available: {len(main_df[main_df['lxAiUsage'] == 'aiAvailable'])}")
    print(
        f"   • High potential: {len(main_df[main_df['lxAiPotential'].isin(['high', 'veryHigh'])])}"
    )
    print(f"   • High confidence: {len(high_confidence)}")
    print(
        f"   • Machine learning: {len(main_df[main_df['lxAiType'] == 'machineLearning'])}"
    )

    return filename


if __name__ == "__main__":
    print("🚀 UPDATING MAIN EXCEL WITH PROPER AI RESEARCH")
    print("=" * 60)
    print("Using 8-step research methodology from AI Research Tracker")
    print("=" * 60)

    # Update main Excel file
    final_file = update_main_excel_with_proper_research()

    print(f"\n🎉 UPDATE COMPLETE!")
    print(f"📋 Files created:")
    print(f"   • {final_file} - Main Excel file with proper AI research")
    print(f"   • proper_ai_research_results.xlsx - Detailed research results")
    print(f"   • ai_research_tracker.xlsx - Research planning and tracking")

    print(f"\n📈 NEXT STEPS:")
    print(f"   1. Review high confidence results (7 apps)")
    print(f"   2. Verify AI-enabled classifications (6 apps)")
    print(f"   3. Check high potential apps (19 apps)")
    print(f"   4. Plan detailed research for low confidence cases")
    print(f"   5. Update classifications based on additional research")
