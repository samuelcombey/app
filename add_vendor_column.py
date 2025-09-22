#!/usr/bin/env python3
"""
Add a Vendor column immediately after Description in the App Directory Excel.
Vendor is inferred from the Official URL using domain-based heuristics and mappings.
"""

import sys
from datetime import datetime
from urllib.parse import urlparse

import pandas as pd


def extract_vendor_from_url(official_url: str) -> str:
    """Infer vendor name from an Official URL using simple, robust heuristics."""
    if (
        not isinstance(official_url, str)
        or not official_url.strip()
        or official_url.strip().upper() == "N/A"
    ):
        return ""

    try:
        parsed = urlparse(official_url.strip())
        host = (parsed.hostname or "").lower()
        if not host:
            return ""

        # Strip common non-brand subdomains
        # Keep only last 3 labels max to simplify logic
        labels = host.split(".")
        if len(labels) > 3:
            labels = labels[-3:]
        if labels and labels[0] in {
            "www",
            "docs",
            "developer",
            "developers",
            "dev",
            "learn",
            "help",
            "support",
            "business",
            "pages",
            "portal",
            "store",
            "news",
            "about",
            "careers",
            "blog",
            "splunkbase",
        }:
            labels = labels[1:]

        # Handle a few common multi-part TLDs
        multi_tlds = {
            "co.uk",
            "org.uk",
            "gov.uk",
            "ac.uk",
            "com.au",
            "net.au",
            "com.br",
            "com.mx",
            "co.jp",
            "com.cn",
            "com.hk",
            "com.sg",
            "co.in",
            "co.za",
        }

        base_label = ""
        if len(labels) >= 3 and f"{labels[-2]}.{labels[-1]}" in multi_tlds:
            base_label = labels[-3]
        elif len(labels) >= 2:
            base_label = labels[-2]
        elif labels:
            base_label = labels[0]

        if not base_label:
            return ""

        # Normalize by stripping generic suffixes from the base label
        generic_suffixes = (
            "software",
            "solutions",
            "systems",
            "labs",
            "cloud",
            "tech",
            "technologies",
            "apps",
            "app",
            "corp",
            "inc",
            "llc",
            "ltd",
            "group",
            "co",
            "data",
            "networks",
        )

        for suf in generic_suffixes:
            if base_label.endswith(suf) and len(base_label) > len(suf):
                base_label = base_label[: -len(suf)]
                break

        normalized = base_label.strip("-_")

        # Known brand casing / overrides
        overrides = {
            "aws": "AWS",
            "ibm": "IBM",
            "sap": "SAP",
            "vmware": "VMware",
            "github": "GitHub",
            "gitlab": "GitLab",
            "mailchimp": "Mailchimp",
            "zoominfo": "ZoomInfo",
            "xactlycorp": "Xactly",
            "paloaltonetworks": "Palo Alto Networks",
            "jetbrains": "JetBrains",
            "workday": "Workday",
            "salesforce": "Salesforce",
            "adobe": "Adobe",
            "google": "Google",
            "microsoft": "Microsoft",
            "apple": "Apple",
            "amazon": "Amazon",
            "zoominsoftware": "Zoomin",
            "zoomin": "Zoomin",
            "splunk": "Splunk",
            "cisco": "Cisco",
            "meraki": "Meraki",
            "snowflake": "Snowflake",
            "workfront": "Workfront",
            "zendesk": "Zendesk",
            "atlassian": "Atlassian",
            "thoughtworks": "Thoughtworks",
            "oracle": "Oracle",
            "stackoverflow": "Stack Overflow",
        }

        if normalized in overrides:
            return overrides[normalized]

        # Title-case the remaining label heuristically
        def smart_title(s: str) -> str:
            parts = re_split = []
            # Split on dashes/underscores
            re_split = [p for p in re.split(r"[-_]+", s) if p]
            if not re_split:
                return s.title()
            return " ".join(p.capitalize() for p in re_split)

        return smart_title(normalized)
    except Exception:
        return ""


def insert_vendor_column(input_path: str, output_path: str) -> str:
    """Insert Vendor column after Description in the App Directory sheet."""
    # Load workbook via pandas
    df = pd.read_excel(input_path, sheet_name="App Directory")

    # Compute Vendor values
    vendors = []
    for _, row in df.iterrows():
        url = row.get("Official URL", "")
        vendor = extract_vendor_from_url(url)
        vendors.append(vendor)

    # Insert after Description
    if "Vendor" in df.columns:
        df.drop(columns=["Vendor"], inplace=True)

    insert_idx = 0
    if "Description" in df.columns:
        insert_idx = list(df.columns).index("Description") + 1

    left_cols = list(df.columns)[:insert_idx]
    right_cols = list(df.columns)[insert_idx:]
    result_df = pd.concat(
        [df[left_cols], pd.Series(vendors, name="Vendor"), df[right_cols]], axis=1
    )

    # Write back replacing only the App Directory sheet
    with pd.ExcelWriter(output_path, engine="openpyxl", mode="w") as writer:
        # Preserve only the updated App Directory
        result_df.to_excel(writer, sheet_name="App Directory", index=False)

    return output_path


def main():
    # Default to the latest final file produced by homepage analysis
    default_input = (
        "/Users/sam/workspace/app-des/app_directory_final_homepage_analysis.xlsx"
    )
    default_output = (
        "/Users/sam/workspace/app-des/app_directory_final_homepage_with_vendor.xlsx"
    )

    input_path = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_path = sys.argv[2] if len(sys.argv) > 2 else default_output

    out = insert_vendor_column(input_path, output_path)
    print("✅ Vendor column added after Description")
    print(f"📄 Input:  {input_path}")
    print(f"💾 Output: {out}")
    print("📅", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
