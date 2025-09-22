#!/usr/bin/env python3
"""
Validate Vendor names by comparing against homepage brand indicators.
Extract og:site_name, title, and h1 from each Official URL and compare with current Vendor.
Write a mismatch report and an updated Excel with validated Vendor values.
"""

import time
from datetime import datetime
from typing import Dict, Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import difflib

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from add_vendor_column import extract_vendor_from_url


def normalize_brand(s: str) -> str:
    if not isinstance(s, str):
        return ""
    t = s.strip().lower()
    # Remove punctuation
    t = re.sub(r"[\W_]+", " ", t, flags=re.UNICODE)
    # Remove corporate suffixes
    stop = {
        "inc",
        "inc.",
        "llc",
        "l.l.c",
        "ltd",
        "ltd.",
        "limited",
        "corp",
        "corp.",
        "corporation",
        "company",
        "co",
        "co.",
        "gmbh",
        "plc",
        "srl",
        "bv",
        "b.v.",
        "sa",
        "s.a.",
        "pte",
        "pty",
        "ag",
        "nv",
        "oy",
    }
    parts = [p for p in t.split() if p not in stop]
    return " ".join(parts)


def fetch_brand_indicators(url: str) -> Tuple[Dict[str, str], str]:
    if not isinstance(url, str) or not url.strip() or url.strip().upper() == "N/A":
        return {"site_name": "", "title": "", "h1": ""}, "no_url"
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"
            )
        }
        resp = requests.get(url, headers=headers, timeout=10, verify=False)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")

        site_name = ""
        meta_site = soup.find("meta", attrs={"property": "og:site_name"})
        if meta_site and meta_site.get("content"):
            site_name = meta_site.get("content", "").strip()
        if not site_name:
            meta_app = soup.find("meta", attrs={"name": "application-name"})
            if meta_app and meta_app.get("content"):
                site_name = meta_app.get("content", "").strip()

        title = ""
        t = soup.find("title")
        if t and t.get_text():
            title = t.get_text().strip()

        h1_text = ""
        h1 = soup.find("h1")
        if h1 and h1.get_text():
            h1_text = h1.get_text().strip()

        return {"site_name": site_name, "title": title, "h1": h1_text}, "ok"
    except requests.exceptions.RequestException as e:
        return {"site_name": "", "title": "", "h1": ""}, f"request_error: {e}"
    except Exception as e:
        return {"site_name": "", "title": "", "h1": ""}, f"parse_error: {e}"


def pick_best_brand(indicators: Dict[str, str], url: str) -> str:
    candidates = [
        indicators.get("site_name", ""),
        indicators.get("title", ""),
        indicators.get("h1", ""),
    ]
    # Clean candidates - remove delimiters like " | " or " – " and pick leading chunk
    cleaned = []
    for c in candidates:
        c = c or ""
        c = re.split(r"\s[\-|–|—|:|•|·]\s", c)[0].strip()
        cleaned.append(c)
    for c in cleaned:
        if len(normalize_brand(c)) >= 2:
            return c
    # Fallback to domain-based brand
    return extract_vendor_from_url(url)


def compare_vendor(vendor: str, brand: str) -> Tuple[str, float, bool]:
    v = normalize_brand(vendor)
    b = normalize_brand(brand)
    if not b and v:
        return "unknown_brand", 0.0, False
    if v == b and v != "":
        return "exact", 1.0, True
    if v and b and (v in b or b in v):
        return "substring", 1.0, True
    ratio = difflib.SequenceMatcher(None, v, b).ratio() if v or b else 0.0
    if ratio >= 0.86:
        return "fuzzy", ratio, True
    return "mismatch", ratio, False


def validate_and_update(input_path: str, output_report: str, output_excel: str) -> None:
    df = pd.read_excel(input_path, sheet_name="App Directory")

    rows = []
    counts = {
        "total": 0,
        "exact": 0,
        "substring": 0,
        "fuzzy": 0,
        "mismatch": 0,
        "failed": 0,
    }

    for idx, row in df.iterrows():
        counts["total"] += 1
        app = row.get("Name", "")
        url = row.get("Official URL", "")
        current_vendor = row.get("Vendor", "")

        indicators, status = fetch_brand_indicators(url)
        if status != "ok":
            counts["failed"] += 1
        best_brand = pick_best_brand(indicators, url)
        cmp_status, score, is_match = compare_vendor(current_vendor, best_brand)
        counts[cmp_status] = counts.get(cmp_status, 0) + 1

        suggested_vendor = current_vendor
        confidence = (
            "high"
            if cmp_status in {"exact", "substring"}
            else ("medium" if cmp_status == "fuzzy" else "low")
        )
        note = cmp_status
        if not is_match and best_brand:
            suggested_vendor = best_brand
            note = f"suggest_replace (ratio={score:.2f})"

        rows.append(
            {
                "App Name": app,
                "Official URL": url,
                "Vendor (Current)": current_vendor,
                "Brand og:site_name": indicators.get("site_name", ""),
                "Brand <title>": indicators.get("title", ""),
                "Brand <h1>": indicators.get("h1", ""),
                "Best Brand": best_brand,
                "Match Status": cmp_status,
                "Similarity": f"{score:.2f}",
                "Confidence": confidence,
                "Suggested Vendor": suggested_vendor,
                "Fetch Status": status,
            }
        )

        # Be polite with remote servers
        if (idx + 1) % 25 == 0:
            print(f"Validated {idx + 1}/{len(df)} apps...")
        time.sleep(0.5)

    report_df = pd.DataFrame(rows)

    # Write report with summary
    with pd.ExcelWriter(output_report, engine="openpyxl") as writer:
        report_df.to_excel(writer, sheet_name="Validation Results", index=False)
        summary_df = pd.DataFrame(
            {
                "Metric": [
                    "Total",
                    "Exact",
                    "Substring",
                    "Fuzzy",
                    "Mismatch",
                    "Fetch Failed",
                ],
                "Count": [
                    counts["total"],
                    counts["exact"],
                    counts["substring"],
                    counts["fuzzy"],
                    counts["mismatch"],
                    counts["failed"],
                ],
            }
        )
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

    # Update the main Excel's Vendor with suggested where mismatch
    updated_df = df.copy()
    suggested_map = {r["App Name"]: r["Suggested Vendor"] for r in rows}
    for i, r in updated_df.iterrows():
        app = r.get("Name", "")
        suggested = suggested_map.get(app, r.get("Vendor", ""))
        if isinstance(suggested, str) and suggested.strip():
            updated_df.at[i, "Vendor"] = suggested

    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        updated_df.to_excel(writer, sheet_name="App Directory", index=False)

    print("\nValidation complete.")
    print(f"Report:   {output_report}")
    print(f"Corrected: {output_excel}")
    print("Counts:", counts)


def main():
    input_path = (
        "/Users/sam/workspace/app-des/app_directory_final_homepage_with_vendor.xlsx"
    )
    output_report = "/Users/sam/workspace/app-des/vendor_validation_report.xlsx"
    output_excel = "/Users/sam/workspace/app-des/app_directory_final_homepage_with_vendor_validated.xlsx"
    validate_and_update(input_path, output_report, output_excel)


if __name__ == "__main__":
    print("🔎 Vendor Validation Tool")
    print("=" * 40)
    print("Starting validation with homepage brand indicators...")
    main()
