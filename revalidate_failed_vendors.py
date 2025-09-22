#!/usr/bin/env python3
"""
Re-validate vendor names for previously fetch-failed sites by trying
homepage and common About pages with robust headers, then rebuild the
validation report and corrected Excel.
"""

import time
from datetime import datetime
from typing import Dict, List, Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import re
import difflib

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from add_vendor_column import extract_vendor_from_url

# Optional tougher fetcher for anti-bot sites
try:
    import cloudscraper  # type: ignore

    HAVE_CLOUDSCRAPER = True
except Exception:
    HAVE_CLOUDSCRAPER = False


def normalize_brand(s: str) -> str:
    if not isinstance(s, str):
        return ""
    t = s.strip().lower()
    t = re.sub(r"[\W_]+", " ", t, flags=re.UNICODE)
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


def build_candidate_urls(original_url: str) -> List[str]:
    if not isinstance(original_url, str) or not original_url.strip():
        return []
    try:
        p = urlparse(original_url)
        scheme = p.scheme or "https"
        host = p.hostname or ""
        if not host:
            return []

        # registrable domain heuristic (simple)
        labels = host.split(".")
        registrable = None
        if len(labels) >= 2:
            registrable = ".".join(labels[-2:])
        else:
            registrable = host

        hosts = [host]
        if not host.startswith("www."):
            hosts.append("www." + host)
        else:
            hosts.append(host.replace("www.", "", 1))

        # Also try registrable
        if registrable not in hosts:
            hosts.append(registrable)
        if not registrable.startswith("www."):
            hosts.append("www." + registrable)

        paths = [
            "/",
            "/about",
            "/about-us",
            "/aboutus",
            "/company",
            "/en/about",
            "/en/company",
            "/who-we-are",
            "/about/company",
            "/about/company/overview",
        ]

        schemes = [scheme]
        if scheme == "https":
            schemes.append("http")
        else:
            schemes.append("https")

        candidates = []
        for s in schemes:
            for h in hosts:
                for path in paths:
                    candidates.append(urlunparse((s, h, path, "", "", "")))
        return list(dict.fromkeys(candidates))
    except Exception:
        return []


def fetch_brand_indicators(url: str) -> Tuple[Dict[str, str], str]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
    }

    def parse_html(content: bytes) -> Dict[str, str]:
        soup = BeautifulSoup(content, "html.parser")
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
        return {"site_name": site_name, "title": title, "h1": h1_text}

    # Attempt 1: requests
    try:
        resp = requests.get(url, headers=headers, timeout=12, verify=False)
        resp.raise_for_status()
        indicators = parse_html(resp.content)
        return indicators, "ok"
    except requests.exceptions.RequestException as e:
        last_err = f"request_error: {e}"
    except Exception as e:
        last_err = f"parse_error: {e}"

    # Attempt 2: cloudscraper fallback
    if HAVE_CLOUDSCRAPER:
        try:
            scraper = cloudscraper.create_scraper()
            resp2 = scraper.get(url, headers=headers, timeout=16)
            if getattr(resp2, "status_code", 599) and 200 <= resp2.status_code < 300:
                indicators = parse_html(resp2.content)
                return indicators, "ok-cloudscraper"
            last_err = f"cloudscraper_status: {getattr(resp2, 'status_code', 'n/a')}"
        except Exception as e2:
            last_err = f"cloudscraper_error: {e2}"

    return {"site_name": "", "title": "", "h1": ""}, last_err


def pick_best_brand(indicators: Dict[str, str], url: str) -> str:
    candidates = [
        indicators.get("site_name", ""),
        indicators.get("title", ""),
        indicators.get("h1", ""),
    ]
    cleaned = []
    for c in candidates:
        c = c or ""
        c = re.split(r"\s[\-|–|—|:|•|·]\s", c)[0].strip()
        cleaned.append(c)
    for c in cleaned:
        if len(normalize_brand(c)) >= 2:
            return c
    return extract_vendor_from_url(url)


def revalidate_failed(
    input_report: str, input_excel: str, output_report: str, output_excel: str
) -> None:
    prev_df = pd.read_excel(input_report, sheet_name="Validation Results")
    failed_df = prev_df[prev_df["Fetch Status"] != "ok"].copy()

    improved_rows = []
    total_failed = len(failed_df)
    for idx, r in failed_df.iterrows():
        app = r.get("App Name", "")
        url = r.get("Official URL", "")
        current_vendor = r.get("Vendor (Current)", "")

        candidates = build_candidate_urls(url)
        best_indicators = {"site_name": "", "title": "", "h1": ""}
        final_status = "no_attempts"
        for attempt_url in candidates:
            indicators, status = fetch_brand_indicators(attempt_url)
            if status == "ok" and any(indicators.values()):
                best_indicators = indicators
                final_status = f"ok:{attempt_url}"
                break
            final_status = status
            # be polite / avoid rate limits
            time.sleep(0.2)

        best_brand = pick_best_brand(best_indicators, url)
        cmp_status, score, is_match = compare_vendor(current_vendor, best_brand)
        confidence = (
            "high"
            if cmp_status in {"exact", "substring"}
            else ("medium" if cmp_status == "fuzzy" else "low")
        )
        suggested_vendor = current_vendor if is_match or not best_brand else best_brand

        improved_rows.append(
            {
                "App Name": app,
                "Official URL": url,
                "Vendor (Current)": current_vendor,
                "Brand og:site_name": best_indicators.get("site_name", ""),
                "Brand <title>": best_indicators.get("title", ""),
                "Brand <h1>": best_indicators.get("h1", ""),
                "Best Brand": best_brand,
                "Match Status": cmp_status,
                "Similarity": f"{score:.2f}",
                "Confidence": confidence,
                "Suggested Vendor": suggested_vendor,
                "Fetch Status": final_status,
            }
        )

        if (idx + 1) % 10 == 0 or (idx + 1) == total_failed:
            print(f"Revalidated {idx + 1}/{total_failed} failed URLs...")
            try:
                import sys as _sys

                _sys.stdout.flush()
            except Exception:
                pass

    improved_df = pd.DataFrame(improved_rows)

    # Merge improved rows back into previous report
    merged = prev_df.set_index(["App Name"]).copy()
    for _, r in improved_df.iterrows():
        merged.loc[r["App Name"]] = r
    merged = merged.reset_index()

    # Write rerun report
    with pd.ExcelWriter(output_report, engine="openpyxl") as writer:
        merged.to_excel(writer, sheet_name="Validation Results", index=False)
        # Summary
        counts = {
            "total": len(merged),
            "exact": int((merged["Match Status"] == "exact").sum()),
            "substring": int((merged["Match Status"] == "substring").sum()),
            "fuzzy": int((merged["Match Status"] == "fuzzy").sum()),
            "mismatch": int((merged["Match Status"] == "mismatch").sum()),
            "failed": int(
                ~merged["Fetch Status"].astype(str).str.startswith("ok")
            ).sum(),
        }
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

    # Update Excel vendors where suggested differs
    df_main = pd.read_excel(input_excel, sheet_name="App Directory")
    sugg_map = {
        r["App Name"]: r["Suggested Vendor"]
        for _, r in merged.iterrows()
        if str(r.get("Suggested Vendor", "")).strip()
    }
    for i, row in df_main.iterrows():
        app = row.get("Name", "")
        suggested = sugg_map.get(app)
        if isinstance(suggested, str) and suggested.strip():
            df_main.at[i, "Vendor"] = suggested

    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        df_main.to_excel(writer, sheet_name="App Directory", index=False)

    print("Revalidation complete.")
    print(f"Rerun report: {output_report}")
    print(f"Updated Excel: {output_excel}")


def main():
    input_report = "/Users/sam/workspace/app-des/vendor_validation_report.xlsx"
    input_excel = "/Users/sam/workspace/app-des/app_directory_final_homepage_with_vendor_validated.xlsx"
    output_report = "/Users/sam/workspace/app-des/vendor_validation_report_rerun.xlsx"
    output_excel = "/Users/sam/workspace/app-des/app_directory_final_homepage_with_vendor_revalidated.xlsx"
    revalidate_failed(input_report, input_excel, output_report, output_excel)


if __name__ == "__main__":
    print("🔁 Re-validating fetch-failed sites...")
    main()
    print("Done.")
