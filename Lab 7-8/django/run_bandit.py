#!/usr/bin/env python3
import subprocess
import json
import csv
import os

# Read commit IDs from the file
with open('commit_list.txt', 'r') as f:
    commits = [line.strip() for line in f if line.strip()]

results = []

for commit in commits:
    print(f"Checking out commit: {commit}")
    # Checkout the specific commit
    subprocess.run(['git', 'checkout', commit], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Run bandit on the entire repository (recursive scan)
    print(f"Running bandit on commit: {commit}")
    proc = subprocess.run(['bandit', '-r', '.', '-f', 'json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = proc.stdout.decode('utf-8')

    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        print(f"JSON decode error on commit {commit}")
        data = {}

    # Initialize counters for severity and confidence
    high_sev = medium_sev = low_sev = 0
    high_conf = medium_conf = low_conf = 0
    cwes = set()

    # Process each issue detected by bandit
    for issue in data.get('results', []):
        severity = issue.get('issue_severity', '').lower()
        confidence = issue.get('issue_confidence', '').lower()
        cwe = issue.get('cwe', 'N/A')
        cwes.add(cwe)

        if severity == 'high':
            high_sev += 1
        elif severity == 'medium':
            medium_sev += 1
        elif severity == 'low':
            low_sev += 1

        if confidence == 'high':
            high_conf += 1
        elif confidence == 'medium':
            medium_conf += 1
        elif confidence == 'low':
            low_conf += 1

    results.append({
        'commit': commit,
        'high_severity': high_sev,
        'medium_severity': medium_sev,
        'low_severity': low_sev,
        'high_confidence': high_conf,
        'medium_confidence': medium_conf,
        'low_confidence': low_conf,
        'unique_cwes': ";".join(cwes)
    })

# Return to the main branch after processing
print("Returning to main branch...")
subprocess.run(['git', 'checkout', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Write results to a CSV file
csv_file = 'bandit_results.csv'
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['commit', 'high_severity', 'medium_severity', 'low_severity',
                  'high_confidence', 'medium_confidence', 'low_confidence', 'unique_cwes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Bandit analysis completed. Results saved in {csv_file}")
