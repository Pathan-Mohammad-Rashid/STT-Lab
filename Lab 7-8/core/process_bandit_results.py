#!/usr/bin/env python3
import os
import json
import csv
import glob

# List to hold aggregated results from each commit
results = []

# Loop over each JSON file in the bandit_result folder
for filepath in glob.glob("bandit_result/bandit_output_*.json"):
    # Extract commit hash from the filename (assumes format: bandit_output_<commit-hash>.json)
    filename = os.path.basename(filepath)
    commit_hash = filename.replace("bandit_output_", "").replace(".json", "")
    print(f"Processing commit: {commit_hash}")
    
    # Load the JSON content from the file
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {filepath}")
        continue

    # Initialize counters for vulnerability metrics
    high_sev = medium_sev = low_sev = 0
    high_conf = medium_conf = low_conf = 0
    cwes = set()

    # Process each issue reported by bandit
    for issue in data.get("results", []):
        severity = issue.get("issue_severity", "").lower()
        confidence = issue.get("issue_confidence", "").lower()
        cwe = issue.get("cwe", "N/A")
        cwes.add(cwe)
        
        if severity == "high":
            high_sev += 1
        elif severity == "medium":
            medium_sev += 1
        elif severity == "low":
            low_sev += 1

        if confidence == "high":
            high_conf += 1
        elif confidence == "medium":
            medium_conf += 1
        elif confidence == "low":
            low_conf += 1

    # Append the commit's aggregated metrics to our results list
    results.append({
        "commit": commit_hash,
        "high_severity": high_sev,
        "medium_severity": medium_sev,
        "low_severity": low_sev,
        "high_confidence": high_conf,
        "medium_confidence": medium_conf,
        "low_confidence": low_conf,
        "unique_cwes": ";".join(sorted(cwes))
    })

# Write the aggregated results to a CSV file
csv_file = "aggregated_bandit_results.csv"
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ["commit", "high_severity", "medium_severity", "low_severity",
                  "high_confidence", "medium_confidence", "low_confidence", "unique_cwes"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Aggregated bandit analysis saved in {csv_file}")
