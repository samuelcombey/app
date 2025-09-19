#!/usr/bin/env python3
"""
Comprehensive AI Research Plan for verifying AI capabilities of all applications.
"""

import pandas as pd
import openpyxl
from datetime import datetime
import time


def create_research_plan():
    """Create a structured research plan for AI verification"""

    print("🔬 AI CAPABILITIES RESEARCH PLAN")
    print("=" * 50)

    # Read current Excel file
    df = pd.read_excel("app_directory_with_ai_data.xlsx")

    print(f"📊 Target: {len(df)} applications to research")
    print(
        f"📅 Research Period: {datetime.now().strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}"
    )

    # Phase 1: Prioritization
    print("\n🎯 PHASE 1: PRIORITIZATION")
    print("-" * 30)

    # Categorize apps by research priority
    high_priority = []
    medium_priority = []
    low_priority = []

    for _, row in df.iterrows():
        app_name = row["Name"]
        description = row["Description"]

        # High Priority: Known AI companies or obvious AI apps
        if any(
            keyword in app_name.lower()
            for keyword in [
                "ai",
                "ml",
                "machine learning",
                "neural",
                "intelligence",
                "smart",
                "predictive",
                "analytics",
                "automation",
            ]
        ) or any(
            keyword in description.lower()
            for keyword in [
                "artificial intelligence",
                "machine learning",
                "neural network",
                "deep learning",
                "ai-powered",
                "intelligent",
                "predictive",
            ]
        ):
            high_priority.append(app_name)

        # Medium Priority: Major enterprise platforms
        elif any(
            keyword in app_name.lower()
            for keyword in [
                "salesforce",
                "microsoft",
                "adobe",
                "google",
                "amazon",
                "oracle",
                "ibm",
                "sap",
                "servicenow",
                "workday",
                "zoom",
                "slack",
            ]
        ):
            medium_priority.append(app_name)

        # Low Priority: Basic utilities and tools
        else:
            low_priority.append(app_name)

    print(f"🔴 High Priority: {len(high_priority)} apps")
    print(f"🟡 Medium Priority: {len(medium_priority)} apps")
    print(f"🟢 Low Priority: {len(low_priority)} apps")

    # Phase 2: Research Methodology
    print("\n🔬 PHASE 2: RESEARCH METHODOLOGY")
    print("-" * 35)

    research_steps = [
        "1. Official Website Analysis",
        "2. Product Documentation Review",
        "3. Feature List Verification",
        "4. Recent Announcements Check",
        "5. AI Partnership Research",
        "6. User Review Analysis",
        "7. Technical Documentation Review",
        "8. Expert Consultation",
    ]

    for step in research_steps:
        print(f"   {step}")

    # Phase 3: Research Framework
    print("\n📋 PHASE 3: RESEARCH FRAMEWORK")
    print("-" * 32)

    research_criteria = {
        "AI Potential": {
            "veryHigh": "Advanced AI features, ML/AI core functionality",
            "high": "Significant AI capabilities, AI-powered features",
            "medium": "Some AI features, AI integration available",
            "low": "Limited or no AI capabilities",
        },
        "AI Risk": {
            "unacceptable": "Critical systems, high data sensitivity",
            "high": "Sensitive data, compliance requirements",
            "limited": "Moderate data handling, some privacy concerns",
            "minimal": "Low risk, basic functionality",
        },
        "AI Usage": {
            "aiEnabled": "Active AI features currently available",
            "aiAvailable": "AI capabilities exist but not primary",
            "noAiUsage": "No current AI features",
            "unknown": "Unable to determine from research",
        },
        "AI Type": {
            "llm": "Large Language Models, NLP, text generation",
            "neuralNet": "Neural networks, deep learning",
            "machineLearning": "ML algorithms, predictive analytics",
            "Other": "Other AI types or general AI",
        },
    }

    for category, criteria in research_criteria.items():
        print(f"\n📊 {category}:")
        for level, description in criteria.items():
            print(f"   • {level}: {description}")

    # Phase 4: Research Schedule
    print("\n📅 PHASE 4: RESEARCH SCHEDULE")
    print("-" * 32)

    total_apps = len(df)
    apps_per_day = 20  # Realistic research pace
    total_days = (total_apps // apps_per_day) + 1

    print(f"📊 Research Pace: {apps_per_day} apps per day")
    print(f"📅 Estimated Duration: {total_days} days")
    print(f"⏰ Daily Time Investment: 4-6 hours")

    # Phase 5: Quality Assurance
    print("\n✅ PHASE 5: QUALITY ASSURANCE")
    print("-" * 35)

    qa_steps = [
        "1. Cross-reference multiple sources",
        "2. Verify with official documentation",
        "3. Check for recent updates/announcements",
        "4. Validate with domain experts",
        "5. Review and update classifications",
        "6. Document research sources",
        "7. Flag uncertain classifications",
    ]

    for step in qa_steps:
        print(f"   {step}")

    # Phase 6: Research Tools and Resources
    print("\n🛠️  PHASE 6: RESEARCH TOOLS & RESOURCES")
    print("-" * 40)

    research_resources = {
        "Official Sources": [
            "Company websites",
            "Product documentation",
            "Feature lists",
            "Release notes",
            "AI/ML product pages",
        ],
        "Third-Party Sources": [
            "G2 reviews and features",
            "Capterra product information",
            "TechCrunch AI coverage",
            "VentureBeat AI news",
            "Industry analyst reports",
        ],
        "Technical Sources": [
            "GitHub repositories",
            "API documentation",
            "Developer resources",
            "Technical blogs",
            "Open source projects",
        ],
        "Expert Sources": [
            "Industry experts",
            "AI/ML practitioners",
            "Product managers",
            "Technical consultants",
            "User communities",
        ],
    }

    for category, sources in research_resources.items():
        print(f"\n📚 {category}:")
        for source in sources:
            print(f"   • {source}")

    # Create research tracking spreadsheet
    create_research_tracker(df, high_priority, medium_priority, low_priority)

    return df


def create_research_tracker(df, high_priority, medium_priority, low_priority):
    """Create a research tracking spreadsheet"""

    # Create research tracker DataFrame
    tracker_data = []

    for _, row in df.iterrows():
        app_name = row["Name"]

        # Determine priority
        if app_name in high_priority:
            priority = "High"
        elif app_name in medium_priority:
            priority = "Medium"
        else:
            priority = "Low"

        tracker_data.append(
            {
                "App Name": app_name,
                "Priority": priority,
                "Research Status": "Not Started",
                "Research Date": "",
                "AI Potential": "",
                "AI Risk": "",
                "AI Usage": "",
                "AI Type": "",
                "AI Description": "",
                "Research Sources": "",
                "Notes": "",
                "Verified": "No",
            }
        )

    tracker_df = pd.DataFrame(tracker_data)

    # Create Excel file with research tracker
    filename = "ai_research_tracker.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main tracker sheet
        tracker_df.to_excel(writer, sheet_name="Research Tracker", index=False)

        # Priority sheets
        high_priority_df = tracker_df[tracker_df["Priority"] == "High"]
        medium_priority_df = tracker_df[tracker_df["Priority"] == "Medium"]
        low_priority_df = tracker_df[tracker_df["Priority"] == "Low"]

        high_priority_df.to_excel(writer, sheet_name="High Priority", index=False)
        medium_priority_df.to_excel(writer, sheet_name="Medium Priority", index=False)
        low_priority_df.to_excel(writer, sheet_name="Low Priority", index=False)

        # Research guidelines sheet
        guidelines_data = {
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

        guidelines_df = pd.DataFrame(guidelines_data)
        guidelines_df.to_excel(writer, sheet_name="Research Guidelines", index=False)

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

    print(f"\n📋 Research Tracker Created: {filename}")
    print(f"   • {len(tracker_df)} apps to research")
    print(f"   • Priority-based organization")
    print(f"   • Research guidelines included")
    print(f"   • Progress tracking ready")

    return filename


if __name__ == "__main__":
    print("🔬 Creating Comprehensive AI Research Plan...")
    tracker_file = create_research_plan()

    print(f"\n🎉 Research Plan Complete!")
    print(f"📋 Next Steps:")
    print(f"   1. Review the research tracker: {tracker_file}")
    print(f"   2. Start with High Priority apps")
    print(f"   3. Follow the research guidelines")
    print(f"   4. Document all findings")
    print(f"   5. Verify with multiple sources")
    print(f"   6. Update classifications based on real research")
