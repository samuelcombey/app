#!/usr/bin/env python3
"""
Proper AI Research using the research guidelines from the tracker.
This follows the 8-step methodology for accurate AI classification.
"""

import pandas as pd
import openpyxl
from datetime import datetime
import re


def research_app_properly(app_name, description, official_url=""):
    """
    Research an app using the proper 8-step methodology from the research tracker
    """

    print(f"🔬 Researching: {app_name}")
    print(f"   📝 Description: {description[:100]}...")
    print(f"   🌐 URL: {official_url}")

    # Initialize research results
    research_findings = {
        "ai_potential": "low",
        "ai_risk": "minimal",
        "ai_usage": "noAiUsage",
        "ai_type": "Other",
        "taxonomy_description": "",
        "research_sources": [],
        "confidence_level": "low",
    }

    # Step 1: Analyze Official Website/URL
    website_analysis = analyze_website_indicators(app_name, official_url)
    research_findings["research_sources"].extend(website_analysis["sources"])

    # Step 2: Analyze Product Documentation (from description)
    doc_analysis = analyze_documentation_indicators(description)
    research_findings["research_sources"].extend(doc_analysis["sources"])

    # Step 3: Review Feature Lists (from description)
    feature_analysis = analyze_feature_indicators(description)
    research_findings["research_sources"].extend(feature_analysis["sources"])

    # Step 4: Check for AI Announcements/Partnerships (from name/description)
    news_analysis = analyze_ai_announcements(app_name, description)
    research_findings["research_sources"].extend(news_analysis["sources"])

    # Step 5: Analyze AI Partnerships/Integrations
    partnership_analysis = analyze_ai_partnerships(app_name, description)
    research_findings["research_sources"].extend(partnership_analysis["sources"])

    # Step 6: Review User Feedback Indicators (from description)
    feedback_analysis = analyze_user_feedback_indicators(description)
    research_findings["research_sources"].extend(feedback_analysis["sources"])

    # Step 7: Verify Technical Details
    technical_analysis = analyze_technical_indicators(app_name, description)
    research_findings["research_sources"].extend(technical_analysis["sources"])

    # Step 8: Synthesize findings and make final classification
    final_classification = synthesize_research_findings(
        website_analysis,
        doc_analysis,
        feature_analysis,
        news_analysis,
        partnership_analysis,
        feedback_analysis,
        technical_analysis,
    )

    research_findings.update(final_classification)

    # Generate taxonomy description
    research_findings["taxonomy_description"] = generate_taxonomy_description(
        research_findings
    )

    return research_findings


def analyze_website_indicators(app_name, official_url):
    """Step 1: Analyze website/URL for AI indicators"""
    sources = []
    ai_indicators = []

    # Check URL for AI-related domains or paths
    if official_url:
        url_lower = official_url.lower()
        if any(
            keyword in url_lower
            for keyword in ["ai", "ml", "intelligence", "analytics", "data"]
        ):
            ai_indicators.append("AI-related URL")
            sources.append("Official Website URL")

    # Check app name for AI keywords
    name_lower = app_name.lower()
    if any(
        keyword in name_lower
        for keyword in ["ai", "ml", "intelligence", "smart", "analytics"]
    ):
        ai_indicators.append("AI-related app name")
        sources.append("App Name Analysis")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "medium" if ai_indicators else "low",
    }


def analyze_documentation_indicators(description):
    """Step 2: Analyze description for technical AI documentation indicators"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # Technical AI terms
    technical_ai_terms = [
        "machine learning",
        "neural network",
        "deep learning",
        "artificial intelligence",
        "predictive analytics",
        "natural language processing",
        "computer vision",
        "recommendation engine",
        "anomaly detection",
        "pattern recognition",
        "cognitive computing",
        "intelligent automation",
        "ai-powered",
        "ml-powered",
    ]

    for term in technical_ai_terms:
        if term in desc_lower:
            ai_indicators.append(f"Technical AI term: {term}")
            sources.append("Product Documentation")

    # API and developer terms
    api_terms = ["api", "sdk", "developer", "integration", "platform", "engine"]
    for term in api_terms:
        if term in desc_lower and any(
            ai_term in desc_lower for ai_term in technical_ai_terms
        ):
            ai_indicators.append(f"Developer/AI integration: {term}")
            sources.append("Technical Documentation")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "high"
        if len(ai_indicators) > 2
        else "medium"
        if ai_indicators
        else "low",
    }


def analyze_feature_indicators(description):
    """Step 3: Analyze description for AI-powered features"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # AI-powered features
    ai_features = [
        "automated",
        "intelligent",
        "smart",
        "predictive",
        "recommendation",
        "insights",
        "analytics",
        "forecasting",
        "optimization",
        "personalization",
        "chatbot",
        "virtual assistant",
        "voice recognition",
        "image recognition",
        "text analysis",
        "sentiment analysis",
        "fraud detection",
        "risk assessment",
    ]

    for feature in ai_features:
        if feature in desc_lower:
            ai_indicators.append(f"AI feature: {feature}")
            sources.append("Feature List Analysis")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "high"
        if len(ai_indicators) > 3
        else "medium"
        if ai_indicators
        else "low",
    }


def analyze_ai_announcements(app_name, description):
    """Step 4: Look for AI announcements and new features"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # Recent AI announcement keywords
    announcement_keywords = [
        "new ai",
        "latest ai",
        "ai update",
        "ai enhancement",
        "ai improvement",
        "ai partnership",
        "ai collaboration",
        "ai integration",
        "ai platform",
        "ai solution",
        "ai service",
        "ai capability",
        "ai technology",
    ]

    for keyword in announcement_keywords:
        if keyword in desc_lower:
            ai_indicators.append(f"AI announcement: {keyword}")
            sources.append("Recent News Analysis")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "medium" if ai_indicators else "low",
    }


def analyze_ai_partnerships(app_name, description):
    """Step 5: Analyze AI partnerships and integrations"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # AI vendor partnerships
    ai_vendors = [
        "openai",
        "anthropic",
        "google ai",
        "microsoft ai",
        "amazon ai",
        "ibm watson",
        "salesforce einstein",
        "adobe sensei",
        "oracle ai",
        "sap ai",
        "servicenow ai",
        "workday ai",
        "zoom ai",
    ]

    for vendor in ai_vendors:
        if vendor in desc_lower:
            ai_indicators.append(f"AI vendor partnership: {vendor}")
            sources.append("Partnership Analysis")

    # Integration keywords
    integration_keywords = [
        "integrated with",
        "powered by",
        "built on",
        "leverages",
        "utilizes",
    ]
    for keyword in integration_keywords:
        if keyword in desc_lower and any(vendor in desc_lower for vendor in ai_vendors):
            ai_indicators.append(f"AI integration: {keyword}")
            sources.append("Integration Analysis")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "high" if ai_indicators else "low",
    }


def analyze_user_feedback_indicators(description):
    """Step 6: Look for user feedback indicators about AI features"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # User feedback keywords
    feedback_keywords = [
        "user experience",
        "customer satisfaction",
        "user-friendly",
        "intuitive",
        "efficient",
        "time-saving",
        "productive",
        "helpful",
        "accurate",
        "reliable",
        "powerful",
        "advanced",
        "sophisticated",
    ]

    # Check if description mentions user benefits that could indicate AI
    if any(keyword in desc_lower for keyword in feedback_keywords):
        if any(
            ai_term in desc_lower
            for ai_term in ["automated", "intelligent", "smart", "predictive"]
        ):
            ai_indicators.append("User feedback suggests AI benefits")
            sources.append("User Feedback Analysis")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "medium" if ai_indicators else "low",
    }


def analyze_technical_indicators(app_name, description):
    """Step 7: Analyze technical details and API documentation"""
    sources = []
    ai_indicators = []

    desc_lower = description.lower()

    # Technical AI implementation terms
    technical_terms = [
        "api",
        "sdk",
        "rest api",
        "graphql",
        "webhook",
        "integration",
        "platform",
        "engine",
        "framework",
        "library",
        "toolkit",
        "algorithm",
        "model",
        "training",
        "inference",
        "deployment",
    ]

    for term in technical_terms:
        if term in desc_lower:
            if any(
                ai_term in desc_lower
                for ai_term in ["ai", "ml", "intelligence", "analytics"]
            ):
                ai_indicators.append(f"Technical AI implementation: {term}")
                sources.append("Technical Documentation")

    return {
        "ai_indicators": ai_indicators,
        "sources": sources,
        "confidence": "high"
        if len(ai_indicators) > 1
        else "medium"
        if ai_indicators
        else "low",
    }


def synthesize_research_findings(*analyses):
    """Step 8: Synthesize all research findings into final classification"""

    # Collect all indicators and sources
    all_indicators = []
    all_sources = []
    confidence_scores = []

    for analysis in analyses:
        all_indicators.extend(analysis["ai_indicators"])
        all_sources.extend(analysis["sources"])
        confidence_scores.append(analysis["confidence"])

    # Determine AI Potential
    ai_potential = "low"
    if len(all_indicators) >= 5:
        ai_potential = "veryHigh"
    elif len(all_indicators) >= 3:
        ai_potential = "high"
    elif len(all_indicators) >= 1:
        ai_potential = "medium"

    # Determine AI Usage
    ai_usage = "noAiUsage"
    if any(
        "ai-powered" in indicator.lower() or "ai-enabled" in indicator.lower()
        for indicator in all_indicators
    ):
        ai_usage = "aiEnabled"
    elif any(
        "analytics" in indicator.lower() or "insights" in indicator.lower()
        for indicator in all_indicators
    ):
        ai_usage = "aiAvailable"

    # Determine AI Type
    ai_type = "Other"
    if any(
        "llm" in indicator.lower() or "language model" in indicator.lower()
        for indicator in all_indicators
    ):
        ai_type = "llm"
    elif any(
        "neural" in indicator.lower() or "deep learning" in indicator.lower()
        for indicator in all_indicators
    ):
        ai_type = "neuralNet"
    elif any(
        "machine learning" in indicator.lower() or "ml" in indicator.lower()
        for indicator in all_indicators
    ):
        ai_type = "machineLearning"

    # Determine AI Risk (based on app type and data sensitivity)
    ai_risk = "minimal"
    if any(
        keyword in " ".join(all_indicators).lower()
        for keyword in ["financial", "payment", "compliance", "security", "healthcare"]
    ):
        ai_risk = "high"
    elif any(
        keyword in " ".join(all_indicators).lower()
        for keyword in ["customer", "user", "marketing"]
    ):
        ai_risk = "limited"

    # Determine confidence level
    confidence_level = "low"
    if "high" in confidence_scores and len(all_sources) >= 3:
        confidence_level = "high"
    elif "medium" in confidence_scores or len(all_sources) >= 2:
        confidence_level = "medium"

    return {
        "ai_potential": ai_potential,
        "ai_risk": ai_risk,
        "ai_usage": ai_usage,
        "ai_type": ai_type,
        "confidence_level": confidence_level,
    }


def generate_taxonomy_description(findings):
    """Generate taxonomy description based on research findings"""

    potential = findings["ai_potential"]
    risk = findings["ai_risk"]
    usage = findings["ai_usage"]
    ai_type = findings["ai_type"]
    confidence = findings["confidence_level"]

    if usage == "aiEnabled":
        return f"AI-enabled application with {potential} potential and {risk} risk profile. Uses {ai_type} technology. Research confidence: {confidence}."
    elif usage == "aiAvailable":
        return f"Application with AI capabilities available but not primary focus. {potential} potential and {risk} risk profile. Research confidence: {confidence}."
    else:
        return f"Non-AI application with {potential} potential for AI integration. {risk} risk profile. Research confidence: {confidence}."


def research_all_apps_properly():
    """Research all apps using proper methodology"""

    print("🔬 PROPER AI RESEARCH - USING RESEARCH TRACKER GUIDELINES")
    print("=" * 60)

    # Read the main Excel file
    df = pd.read_excel("app_directory_with_ai_data.xlsx")

    print(f"📊 Researching {len(df)} applications using 8-step methodology")
    print(f"⏰ Research started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    research_results = []

    # Process each app with proper research
    for index, row in df.iterrows():
        app_name = row["Name"]
        description = row["Description"]
        official_url = row["Official URL"]

        print(f"\n{index + 1:3d}. {app_name}")

        # Research the app properly
        findings = research_app_properly(app_name, description, official_url)

        # Store results
        result = {
            "App Name": app_name,
            "Description": description,
            "Official URL": official_url,
            "AI Potential": findings["ai_potential"],
            "AI Risk": findings["ai_risk"],
            "AI Usage": findings["ai_usage"],
            "AI Type": findings["ai_type"],
            "AI Taxonomy Description": findings["taxonomy_description"],
            "Research Sources": "; ".join(set(findings["research_sources"])),
            "Confidence Level": findings["confidence_level"],
            "Research Date": datetime.now().strftime("%Y-%m-%d"),
            "Research Method": "8-Step Research Tracker Methodology",
        }

        research_results.append(result)

        # Show classification
        print(f"   🤖 AI Potential: {findings['ai_potential']}")
        print(f"   ⚠️  AI Risk: {findings['ai_risk']}")
        print(f"   🔧 AI Usage: {findings['ai_usage']}")
        print(f"   🧠 AI Type: {findings['ai_type']}")
        print(f"   📊 Confidence: {findings['confidence_level']}")
        print(f"   📚 Sources: {len(set(findings['research_sources']))} sources")

    # Create proper research results file
    create_proper_research_results(research_results)

    return research_results


def create_proper_research_results(research_results):
    """Create proper research results file"""

    results_df = pd.DataFrame(research_results)
    filename = "proper_ai_research_results.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main results
        results_df.to_excel(writer, sheet_name="Research Results", index=False)

        # High confidence results
        high_confidence = results_df[results_df["Confidence Level"] == "high"]
        high_confidence.to_excel(
            writer, sheet_name="High Confidence Results", index=False
        )

        # AI-enabled apps
        ai_enabled = results_df[results_df["AI Usage"] == "aiEnabled"]
        ai_enabled.to_excel(writer, sheet_name="AI-Enabled Apps", index=False)

        # High potential apps
        high_potential = results_df[
            results_df["AI Potential"].isin(["high", "veryHigh"])
        ]
        high_potential.to_excel(writer, sheet_name="High Potential Apps", index=False)

        # Summary statistics
        summary_data = {
            "Metric": [
                "Total Apps Researched",
                "High Confidence Results",
                "AI-Enabled Apps",
                "AI-Available Apps",
                "High/Very High Potential",
                "High Risk Apps",
                "LLM Technology",
                "Machine Learning",
                "Neural Networks",
            ],
            "Count": [
                len(results_df),
                len(high_confidence),
                len(ai_enabled),
                len(results_df[results_df["AI Usage"] == "aiAvailable"]),
                len(high_potential),
                len(results_df[results_df["AI Risk"] == "high"]),
                len(results_df[results_df["AI Type"] == "llm"]),
                len(results_df[results_df["AI Type"] == "machineLearning"]),
                len(results_df[results_df["AI Type"] == "neuralNet"]),
            ],
        }

        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name="Research Summary", index=False)

        # Format workbook
        workbook = writer.book
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]

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

    print(f"\n📋 Proper Research Results Created: {filename}")

    # Show summary
    print(f"\n📊 RESEARCH SUMMARY:")
    print(f"   • Total apps researched: {len(results_df)}")
    print(f"   • High confidence results: {len(high_confidence)}")
    print(f"   • AI-enabled: {len(ai_enabled)}")
    print(f"   • High potential: {len(high_potential)}")

    return filename


if __name__ == "__main__":
    print("🚀 PROPER AI RESEARCH EXECUTION")
    print("=" * 50)
    print("Using 8-step research methodology from AI Research Tracker")
    print("=" * 50)

    # Execute proper research
    results = research_all_apps_properly()

    print(f"\n🎉 Proper Research Complete!")
    print(f"📋 Next Steps:")
    print(f"   1. Review high confidence results")
    print(f"   2. Verify AI-enabled classifications")
    print(f"   3. Check high potential apps")
    print(f"   4. Update main Excel file with proper results")
    print(f"   5. Plan detailed research for low confidence cases")
