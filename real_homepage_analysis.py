#!/usr/bin/env python3
"""
Real Homepage Analysis Script
Visit each app's homepage and analyze real content from About pages and descriptions
"""

import pandas as pd
import time
from datetime import datetime
import requests
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_homepage_content(url):
    """
    Fetch and parse the homepage content of an app
    """
    if not url or url == "N/A":
        return None, "No URL provided"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract text content
        text_content = soup.get_text()

        # Look for specific sections
        about_section = ""
        description_section = ""

        # Try to find About section
        about_tags = soup.find_all(
            ["div", "section"], class_=re.compile(r"about|description|overview", re.I)
        )
        for tag in about_tags:
            about_section += tag.get_text() + " "

        # Look for meta description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            description_section = meta_desc.get("content", "")

        # Look for title and h1 tags
        title = soup.find("title")
        h1 = soup.find("h1")

        full_content = f"{title.get_text() if title else ''} {h1.get_text() if h1 else ''} {description_section} {about_section} {text_content[:2000]}"

        return full_content, "Success"

    except requests.exceptions.RequestException as e:
        return None, f"Request failed: {str(e)}"
    except Exception as e:
        return None, f"Parsing failed: {str(e)}"


def analyze_homepage_content(content):
    """
    Analyze the actual homepage content for AI capabilities
    """
    if not content:
        return {
            "ai_potential": "low",
            "ai_risk": "minimal",
            "ai_usage": "noAiUsage",
            "ai_type": "Other",
            "description": "No content available for analysis",
            "confidence": "low",
            "sources": "No content found",
        }

    content_lower = content.lower()

    # AI-related terms found in actual homepage content
    ai_terms = [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "neural network",
        "ai-powered",
        "ai-enabled",
        "intelligent automation",
        "predictive analytics",
        "natural language processing",
        "computer vision",
        "cognitive computing",
        "automated",
        "smart analytics",
        "data science",
        "ml",
        "ai",
        "algorithm",
        "chatbot",
        "conversational ai",
        "recommendation engine",
        "pattern recognition",
    ]

    found_ai_terms = [term for term in ai_terms if term in content_lower]

    if len(found_ai_terms) >= 3:
        return {
            "ai_potential": "veryHigh",
            "ai_risk": "limited",
            "ai_usage": "aiEnabled",
            "ai_type": "machineLearning",
            "description": f"AI-enabled application with multiple AI capabilities: {', '.join(found_ai_terms[:5])}",
            "confidence": "high",
            "sources": "Homepage content analysis",
        }
    elif len(found_ai_terms) == 2:
        return {
            "ai_potential": "high",
            "ai_risk": "limited",
            "ai_usage": "aiEnabled",
            "ai_type": "machineLearning",
            "description": f"AI-enabled application with AI capabilities: {', '.join(found_ai_terms)}",
            "confidence": "high",
            "sources": "Homepage content analysis",
        }
    elif len(found_ai_terms) == 1:
        return {
            "ai_potential": "medium",
            "ai_risk": "minimal",
            "ai_usage": "aiAvailable",
            "ai_type": "Other",
            "description": f"Application with AI capabilities: {found_ai_terms[0]}",
            "confidence": "medium",
            "sources": "Homepage content analysis",
        }

    # Analytics and data terms
    analytics_terms = [
        "analytics",
        "insights",
        "data analysis",
        "business intelligence",
        "reporting",
        "dashboard",
        "metrics",
        "data visualization",
        "statistical analysis",
        "trend analysis",
        "data mining",
    ]

    found_analytics = [term for term in analytics_terms if term in content_lower]

    if found_analytics:
        return {
            "ai_potential": "medium",
            "ai_risk": "minimal",
            "ai_usage": "aiAvailable",
            "ai_type": "Other",
            "description": f"Analytics platform with potential AI capabilities: {', '.join(found_analytics[:3])}",
            "confidence": "low",
            "sources": "Homepage content analysis",
        }

    # Default classification
    return {
        "ai_potential": "low",
        "ai_risk": "minimal",
        "ai_usage": "noAiUsage",
        "ai_type": "Other",
        "description": "Standard application without clear AI indicators in homepage content",
        "confidence": "medium",
        "sources": "Homepage content analysis",
    }


def research_app_homepage(app_name, description, official_url):
    """
    Research a single app by analyzing its actual homepage content
    """
    print(f"🌐 Analyzing homepage for: {app_name}")
    print(f"   📡 URL: {official_url}")

    # Fetch homepage content
    content, status = fetch_homepage_content(official_url)

    if content:
        print(f"   ✅ Content fetched successfully ({len(content)} characters)")
        # Analyze the content
        result = analyze_homepage_content(content)
        print(f"   🔍 Found AI terms: {result['description']}")
    else:
        print(f"   ❌ Failed to fetch content: {status}")
        result = {
            "ai_potential": "low",
            "ai_risk": "minimal",
            "ai_usage": "noAiUsage",
            "ai_type": "Other",
            "description": f"Could not analyze homepage: {status}",
            "confidence": "low",
            "sources": f"Homepage fetch failed: {status}",
        }

    return result


def research_all_apps_homepage():
    """Research all apps by analyzing their actual homepage content"""
    print("🌐 Starting Homepage Content Analysis...")
    print("📅 Research Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Load the current Excel file
    df = pd.read_excel("/Users/sam/workspace/app-des/app_directory_with_ai_data.xlsx")
    print(f"📊 Total apps to research: {len(df)}")

    research_results = []
    high_confidence_count = 0
    medium_confidence_count = 0
    low_confidence_count = 0

    print("\n🔍 Analyzing homepage content for each app...")
    for index, row in df.iterrows():
        app_name = row["Name"]
        description = row["Description"]
        official_url = row["Official URL"]

        print(f"\n--- App {index + 1}/{len(df)} ---")

        # Research this specific app's homepage
        research_result = research_app_homepage(app_name, description, official_url)

        # Create result record
        result = {
            "App Name": app_name,
            "Description": description,
            "Official URL": official_url,
            "AI Potential": research_result["ai_potential"],
            "AI Risk": research_result["ai_risk"],
            "AI Usage": research_result["ai_usage"],
            "AI Type": research_result["ai_type"],
            "AI Taxonomy Description": research_result["description"],
            "Research Sources": research_result["sources"],
            "Confidence Level": research_result["confidence"],
            "Research Date": datetime.now().strftime("%Y-%m-%d"),
            "Research Method": "Homepage Content Analysis + Real Website Data",
        }

        research_results.append(result)

        # Count confidence levels
        if research_result["confidence"] == "high":
            high_confidence_count += 1
        elif research_result["confidence"] == "medium":
            medium_confidence_count += 1
        else:
            low_confidence_count += 1

        # Progress indicator
        if (index + 1) % 10 == 0:
            print(f"\n📈 Progress: {index + 1}/{len(df)} apps analyzed")
            print(f"   🎯 High Confidence: {high_confidence_count}")
            print(f"   🎯 Medium Confidence: {medium_confidence_count}")
            print(f"   🎯 Low Confidence: {low_confidence_count}")

        # Add delay to be respectful to websites
        time.sleep(1)

    print(f"\n📈 Final Homepage Analysis Summary:")
    print(f"   🎯 High Confidence: {high_confidence_count} apps")
    print(f"   🎯 Medium Confidence: {medium_confidence_count} apps")
    print(f"   🎯 Low Confidence: {low_confidence_count} apps")

    # Create results file
    results_df = pd.DataFrame(research_results)
    filename = "/Users/sam/workspace/app-des/homepage_analysis_results.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main results
        results_df.to_excel(writer, sheet_name="Homepage Analysis Results", index=False)

        # High confidence results
        high_confidence = results_df[results_df["Confidence Level"] == "high"]
        high_confidence.to_excel(writer, sheet_name="High Confidence", index=False)

        # AI-enabled apps
        ai_enabled = results_df[results_df["AI Usage"] == "aiEnabled"]
        ai_enabled.to_excel(writer, sheet_name="AI-Enabled Apps", index=False)

        # Summary statistics
        summary_data = {
            "Metric": [
                "Total Apps Analyzed",
                "High Confidence Results",
                "Medium Confidence Results",
                "Low Confidence Results",
                "AI-Enabled Apps",
                "AI-Available Apps",
                "No AI Usage Apps",
                "Very High Potential",
                "High Potential",
                "LLM Technology",
                "Machine Learning",
                "High Risk Apps",
            ],
            "Count": [
                len(results_df),
                high_confidence_count,
                medium_confidence_count,
                low_confidence_count,
                len(results_df[results_df["AI Usage"] == "aiEnabled"]),
                len(results_df[results_df["AI Usage"] == "aiAvailable"]),
                len(results_df[results_df["AI Usage"] == "noAiUsage"]),
                len(results_df[results_df["AI Potential"] == "veryHigh"]),
                len(results_df[results_df["AI Potential"] == "high"]),
                len(results_df[results_df["AI Type"] == "llm"]),
                len(results_df[results_df["AI Type"] == "machineLearning"]),
                len(results_df[results_df["AI Risk"] == "high"]),
            ],
        }

        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name="Homepage Analysis Summary", index=False)

    print(f"\n✅ Homepage analysis completed! Results saved to: {filename}")
    return results_df


def update_main_excel_with_homepage_analysis():
    """Update the main Excel file with homepage analysis results"""
    print("\n📝 Updating main Excel file with homepage analysis results...")

    # Load research results and main file
    research_df = pd.read_excel(
        "/Users/sam/workspace/app-des/homepage_analysis_results.xlsx",
        sheet_name="Homepage Analysis Results",
    )
    main_df = pd.read_excel(
        "/Users/sam/workspace/app-des/app_directory_with_ai_data.xlsx"
    )

    # Create mapping from research results
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

    # Update main DataFrame
    updated_count = 0
    for index, row in main_df.iterrows():
        app_name = row["Name"]
        if app_name in research_mapping:
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

    # Save updated file
    filename = "/Users/sam/workspace/app-des/app_directory_final_homepage_analysis.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Main directory with updated AI data
        main_df.to_excel(writer, sheet_name="App Directory", index=False)

        # Summary sheets
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
                "High Confidence Research",
                "Updated with Homepage Analysis",
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
                len(research_df[research_df["Confidence Level"] == "high"]),
                updated_count,
            ],
        }

        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name="Homepage Analysis Summary", index=False)

        # High confidence results
        high_confidence = research_df[research_df["Confidence Level"] == "high"]
        high_confidence.to_excel(
            writer, sheet_name="High Confidence Results", index=False
        )

        # AI-enabled apps
        ai_enabled = main_df[main_df["lxAiUsage"] == "aiEnabled"]
        ai_enabled.to_excel(writer, sheet_name="AI-Enabled Apps", index=False)

    print(f"✅ Updated {updated_count} apps with homepage analysis data")
    print(f"💾 Final file saved as: {filename}")

    return filename


if __name__ == "__main__":
    print("🌐 Homepage Content Analysis Tool")
    print("=" * 50)

    # Step 1: Research all apps by analyzing homepage content
    research_results = research_all_apps_homepage()

    # Step 2: Update main Excel file
    final_filename = update_main_excel_with_homepage_analysis()

    print("\n🎉 Homepage Content Analysis Complete!")
    print(f"📁 Final Results: {final_filename}")
