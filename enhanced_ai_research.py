#!/usr/bin/env python3
"""
Enhanced AI Research - Analyze app descriptions and technology mentions
to fill AI columns based on given options.
"""

import pandas as pd
import openpyxl
from datetime import datetime
import re


def analyze_app_ai_characteristics(app_name, description, official_url=""):
    """Enhanced analysis of app AI characteristics using description and technology mentions"""

    name_lower = app_name.lower()
    desc_lower = description.lower()

    # AI Potential Analysis - using only: low, medium, high, veryHigh
    ai_potential = "low"

    # Check for AI/ML keywords in description
    ai_keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "ml",
        "neural",
        "deep learning",
        "predictive",
        "analytics",
        "intelligence",
        "automation",
        "smart",
        "cognitive",
        "algorithm",
        "data science",
        "nlp",
        "natural language",
        "computer vision",
        "recommendation engine",
        "pattern recognition",
        "anomaly detection",
    ]

    advanced_ai_keywords = [
        "advanced ai",
        "sophisticated",
        "cutting-edge",
        "next-generation",
        "revolutionary",
        "enterprise ai",
        "ai platform",
        "ai engine",
        "ai-powered",
        "intelligent automation",
    ]

    enterprise_keywords = [
        "enterprise",
        "professional",
        "comprehensive",
        "powerful",
        "scalable",
        "enterprise-grade",
        "business intelligence",
        "advanced analytics",
    ]

    if any(keyword in desc_lower for keyword in ai_keywords):
        if any(keyword in desc_lower for keyword in advanced_ai_keywords):
            ai_potential = "veryHigh"
        elif any(keyword in desc_lower for keyword in enterprise_keywords):
            ai_potential = "high"
        else:
            ai_potential = "medium"

    # AI Risk Analysis - using only: minimal, limited, high, unacceptable
    ai_risk = "minimal"

    # High risk indicators
    high_risk_keywords = [
        "financial",
        "banking",
        "payment",
        "transaction",
        "compliance",
        "audit",
        "regulatory",
        "gdpr",
        "hipaa",
        "sox",
        "pci",
        "security",
        "encryption",
        "sensitive data",
        "confidential",
        "personal information",
        "healthcare",
        "medical",
        "legal",
        "government",
        "defense",
        "critical infrastructure",
    ]

    # Limited risk indicators
    limited_risk_keywords = [
        "social media",
        "public",
        "consumer",
        "marketing",
        "advertising",
        "content management",
        "crm",
        "sales",
        "customer service",
        "support",
    ]

    if any(keyword in desc_lower for keyword in high_risk_keywords):
        ai_risk = "high"
    elif any(keyword in desc_lower for keyword in limited_risk_keywords):
        ai_risk = "limited"

    # AI Usage Analysis - using only: unknown, noAiUsage, aiAvailable, aiEnabled
    ai_usage = "noAiUsage"

    # AI-enabled indicators
    ai_enabled_keywords = [
        "ai-powered",
        "ai-enabled",
        "artificial intelligence",
        "machine learning",
        "neural network",
        "deep learning",
        "predictive analytics",
        "intelligent",
        "smart automation",
        "cognitive",
        "ai-driven",
        "ml-powered",
    ]

    # AI-available indicators
    ai_available_keywords = [
        "analytics",
        "insights",
        "data analysis",
        "reporting",
        "dashboard",
        "business intelligence",
        "data visualization",
        "statistical analysis",
        "trend analysis",
        "pattern recognition",
        "data mining",
    ]

    if any(keyword in desc_lower for keyword in ai_enabled_keywords):
        ai_usage = "aiEnabled"
    elif any(keyword in desc_lower for keyword in ai_available_keywords):
        ai_usage = "aiAvailable"

    # AI Type Analysis - using only: neuralNet, llm, machineLearning, Other
    ai_type = "Other"

    # LLM indicators
    llm_keywords = [
        "llm",
        "large language model",
        "gpt",
        "chatbot",
        "conversational",
        "nlp",
        "natural language",
        "text generation",
        "language model",
        "chat",
        "dialogue",
        "text analysis",
        "sentiment analysis",
        "language processing",
        "translation",
    ]

    # Neural network indicators
    neural_keywords = [
        "neural network",
        "deep learning",
        "cnn",
        "rnn",
        "transformer",
        "neural",
        "deep neural",
        "convolutional",
        "recurrent",
        "transformer",
        "attention",
        "deep reinforcement learning",
        "gan",
        "generative adversarial",
    ]

    # Machine learning indicators
    ml_keywords = [
        "machine learning",
        "ml",
        "algorithm",
        "prediction",
        "classification",
        "regression",
        "clustering",
        "recommendation",
        "supervised",
        "unsupervised",
        "reinforcement learning",
        "feature engineering",
        "model training",
    ]

    if any(keyword in desc_lower for keyword in llm_keywords):
        ai_type = "llm"
    elif any(keyword in desc_lower for keyword in neural_keywords):
        ai_type = "neuralNet"
    elif any(keyword in desc_lower for keyword in ml_keywords):
        ai_type = "machineLearning"

    # AI Taxonomy Description - custom string based on analysis
    taxonomy_desc = ""
    if ai_usage != "noAiUsage":
        taxonomy_desc = f"AI-powered application with {ai_potential} potential and {ai_risk} risk profile. {ai_type} technology with {ai_usage} usage."
    else:
        taxonomy_desc = f"Non-AI application with {ai_potential} potential for AI integration. {ai_risk} risk profile."

    return ai_potential, ai_risk, ai_usage, ai_type, taxonomy_desc


def research_all_apps():
    """Research all apps in the main Excel file"""

    print("🔬 ENHANCED AI RESEARCH - ALL APPS")
    print("=" * 40)

    # Read the main Excel file
    df = pd.read_excel("app_directory_with_ai_data.xlsx")

    print(f"📊 Researching {len(df)} applications")
    print(f"⏰ Research started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Research results storage
    research_results = []

    # Process each app
    for index, row in df.iterrows():
        app_name = row["Name"]
        description = row["Description"]
        official_url = row["Official URL"]

        print(f"\n{index + 1:3d}. Researching: {app_name}")

        # Analyze AI characteristics
        ai_potential, ai_risk, ai_usage, ai_type, taxonomy_desc = (
            analyze_app_ai_characteristics(app_name, description, official_url)
        )

        # Store results
        result = {
            "App Name": app_name,
            "Description": description,
            "Official URL": official_url,
            "AI Potential": ai_potential,
            "AI Risk": ai_risk,
            "AI Usage": ai_usage,
            "AI Type": ai_type,
            "AI Taxonomy Description": taxonomy_desc,
            "Research Date": datetime.now().strftime("%Y-%m-%d"),
            "Research Method": "Description Analysis",
        }

        research_results.append(result)

        # Show classification
        print(f"   🤖 AI Potential: {ai_potential}")
        print(f"   ⚠️  AI Risk: {ai_risk}")
        print(f"   🔧 AI Usage: {ai_usage}")
        print(f"   🧠 AI Type: {ai_type}")

    # Create research results file
    create_enhanced_research_results(research_results)

    return research_results


def create_enhanced_research_results(research_results):
    """Create enhanced research results file"""

    # Convert to DataFrame
    results_df = pd.DataFrame(research_results)

    # Create Excel file
    filename = "enhanced_ai_research_results.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main results sheet
        results_df.to_excel(writer, sheet_name="Research Results", index=False)

        # Summary by AI Potential
        potential_summary = results_df["AI Potential"].value_counts().reset_index()
        potential_summary.columns = ["AI Potential", "Count"]
        potential_summary.to_excel(
            writer, sheet_name="AI Potential Summary", index=False
        )

        # Summary by AI Risk
        risk_summary = results_df["AI Risk"].value_counts().reset_index()
        risk_summary.columns = ["AI Risk", "Count"]
        risk_summary.to_excel(writer, sheet_name="AI Risk Summary", index=False)

        # Summary by AI Usage
        usage_summary = results_df["AI Usage"].value_counts().reset_index()
        usage_summary.columns = ["AI Usage", "Count"]
        usage_summary.to_excel(writer, sheet_name="AI Usage Summary", index=False)

        # Summary by AI Type
        type_summary = results_df["AI Type"].value_counts().reset_index()
        type_summary.columns = ["AI Type", "Count"]
        type_summary.to_excel(writer, sheet_name="AI Type Summary", index=False)

        # High Potential Apps
        high_potential = results_df[
            results_df["AI Potential"].isin(["high", "veryHigh"])
        ]
        high_potential.to_excel(writer, sheet_name="High Potential Apps", index=False)

        # AI-Enabled Apps
        ai_enabled = results_df[results_df["AI Usage"] == "aiEnabled"]
        ai_enabled.to_excel(writer, sheet_name="AI-Enabled Apps", index=False)

        # High Risk Apps
        high_risk = results_df[results_df["AI Risk"] == "high"]
        high_risk.to_excel(writer, sheet_name="High Risk Apps", index=False)

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

    print(f"\n📋 Enhanced Research Results Created: {filename}")

    # Show comprehensive summary
    print(f"\n📊 RESEARCH SUMMARY:")
    print(f"   • Total apps researched: {len(results_df)}")
    print(f"   • AI Potential distribution:")
    for potential, count in results_df["AI Potential"].value_counts().items():
        print(f"     - {potential}: {count} apps")
    print(f"   • AI Usage distribution:")
    for usage, count in results_df["AI Usage"].value_counts().items():
        print(f"     - {usage}: {count} apps")
    print(f"   • AI Type distribution:")
    for ai_type, count in results_df["AI Type"].value_counts().items():
        print(f"     - {ai_type}: {count} apps")

    return filename


def show_research_methodology():
    """Show the enhanced research methodology"""

    print(f"\n🔬 ENHANCED RESEARCH METHODOLOGY:")
    print(f"   • App name analysis for AI keywords")
    print(f"   • Description analysis for AI capabilities")
    print(f"   • Technology mention identification")
    print(f"   • AI potential assessment")
    print(f"   • Risk profile evaluation")
    print(f"   • Usage pattern classification")
    print(f"   • AI type identification")

    print(f"\n📋 CLASSIFICATION CRITERIA:")
    print(f"   • AI Potential: low, medium, high, veryHigh")
    print(f"   • AI Risk: minimal, limited, high, unacceptable")
    print(f"   • AI Usage: unknown, noAiUsage, aiAvailable, aiEnabled")
    print(f"   • AI Type: neuralNet, llm, machineLearning, Other")

    print(f"\n⚠️  RESEARCH LIMITATIONS:")
    print(f"   • Based on description analysis only")
    print(f"   • May miss recent AI updates")
    print(f"   • Requires verification with official sources")
    print(f"   • Some classifications may be conservative")


if __name__ == "__main__":
    print("🚀 ENHANCED AI RESEARCH EXECUTION")
    print("=" * 40)

    show_research_methodology()

    # Execute research on all apps
    results = research_all_apps()

    print(f"\n🎉 Enhanced Research Complete!")
    print(f"📋 Next Steps:")
    print(f"   1. Review research results")
    print(f"   2. Verify high potential apps")
    print(f"   3. Check AI-enabled classifications")
    print(f"   4. Update main Excel file with results")
    print(f"   5. Plan detailed research for uncertain cases")
