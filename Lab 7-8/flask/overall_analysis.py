import os
import json
import subprocess
import datetime
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_commit_date(commit_hash):
    """
    Get the commit date (as a datetime object) for a given commit hash using git.
    Assumes the script is run in the repository's root directory.
    """
    try:
        result = subprocess.run(
            ["git", "show", "-s", "--format=%ci", commit_hash],
            capture_output=True, text=True, check=True
        )
        # Expect date in format "YYYY-MM-DD HH:MM:SS +TZ", so split and take the date part
        date_str = result.stdout.strip().split(' ')[0]  # e.g., "2024-05-01"
        commit_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return commit_date
    except Exception as e:
        print(f"Error retrieving date for commit {commit_hash}: {e}")
        return None

def process_json_files(input_folder):
    """
    Process all Bandit JSON files in the specified folder.
    Each file is expected to be named as 'bandit_output_<commit_hash>.json'.
    Returns a dictionary with commit hashes as keys and extracted data.
    """
    commit_data = {}
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            filepath = os.path.join(input_folder, filename)
            # Extract commit hash from filename
            commit_hash = filename.replace('bandit_output_', '').replace('.json', '')
            with open(filepath, 'r') as file:
                data = json.load(file)
            # Initialize counts for this commit
            confidence = defaultdict(int)
            severity = defaultdict(int)
            cwe_set = set()
            for issue in data.get('results', []):
                conf = issue.get('issue_confidence', 'UNKNOWN')
                sev = issue.get('issue_severity', 'UNKNOWN')
                cwe = issue.get('cwe', 'UNKNOWN')
                confidence[conf] += 1
                severity[sev] += 1
                if cwe != 'UNKNOWN':
                    cwe_set.add(cwe)
            commit_data[commit_hash] = {
                'confidence': dict(confidence),
                'severity': dict(severity),
                'unique_cwes': list(cwe_set)
            }
    return commit_data

def overall_analysis(input_folder, report_output_file):
    """
    Processes all JSON files from the folder, enriches commit data with commit dates,
    performs overall analyses (RQ1, RQ2, RQ3), and saves plots and a text report.
    """
    commit_data = process_json_files(input_folder)
    
    # Enrich each commit entry with the commit date from git
    for commit_hash in commit_data:
        commit_date = get_commit_date(commit_hash)
        commit_data[commit_hash]['date'] = commit_date
    
    # Filter out commits without a valid date
    commit_data = {k: v for k, v in commit_data.items() if v.get('date') is not None}
    
    # -------------------------------
    # RQ1: High Severity Vulnerabilities Over Time
    # -------------------------------
    commit_dates = []
    high_severity_counts = []
    for commit_hash, data in commit_data.items():
        commit_dates.append(data['date'])
        high_count = data['severity'].get("HIGH", 0)
        high_severity_counts.append(high_count)
    
    # Sort by commit date
    sorted_rq1 = sorted(zip(commit_dates, high_severity_counts), key=lambda x: x[0])
    if sorted_rq1:
        dates_sorted, high_counts_sorted = zip(*sorted_rq1)
    else:
        dates_sorted, high_counts_sorted = [], []
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates_sorted, high_counts_sorted, marker='o')
    plt.title("High Severity Vulnerabilities Over Time (RQ1)")
    plt.xlabel("Commit Date")
    plt.ylabel("Number of High Severity Issues")
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.savefig("RQ1_high_severity_over_time.png")
    plt.close()
    
    # -------------------------------
    # RQ2: Vulnerability Trends by Severity (LOW, MEDIUM, HIGH)
    # -------------------------------
    severity_levels = ["LOW", "MEDIUM", "HIGH"]
    severity_counts_by_date = {sev: [] for sev in severity_levels}
    for commit_hash, data in commit_data.items():
        date = data['date']
        for sev in severity_levels:
            count = data['severity'].get(sev, 0)
            severity_counts_by_date[sev].append((date, count))
    
    plt.figure(figsize=(10, 5))
    for sev in severity_levels:
        sorted_points = sorted(severity_counts_by_date[sev], key=lambda x: x[0])
        if sorted_points:
            dates, counts = zip(*sorted_points)
            plt.plot(dates, counts, marker='o', label=sev)
    plt.title("Vulnerability Trends by Severity (RQ2)")
    plt.xlabel("Commit Date")
    plt.ylabel("Number of Issues")
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.savefig("RQ2_vulnerability_trends_by_severity.png")
    plt.close()
    
    # -------------------------------
    # RQ3: Top 10 Most Frequent CWEs
    # -------------------------------
    all_cwes = []
    for data in commit_data.values():
        all_cwes.extend(data.get('unique_cwes', []))
    cwe_counts = Counter(all_cwes)
    top_cwes = cwe_counts.most_common(10)
    if top_cwes:
        cwe_names, frequencies = zip(*top_cwes)
    else:
        cwe_names, frequencies = [], []
    
    plt.figure(figsize=(10, 5))
    plt.bar(cwe_names, frequencies, color='skyblue')
    plt.title("Top 10 Most Frequent CWEs (RQ3)")
    plt.xlabel("CWE Identifier")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.savefig("RQ3_top_cwes.png")
    plt.close()
    
    # -------------------------------
    # Generate Overall Text Report
    # -------------------------------
    with open(report_output_file, 'w') as report:
        report.write("Overall Analysis Report\n")
        report.write("="*40 + "\n\n")
        
        report.write("RQ1: High Severity Vulnerabilities Over Time\n")
        report.write("-" * 50 + "\n")
        report.write("A line plot ('RQ1_high_severity_over_time.png') has been generated, showing the trend of high severity issues over time.\n\n")
        
        report.write("RQ2: Vulnerability Trends by Severity\n")
        report.write("-" * 50 + "\n")
        report.write("A multi-line plot ('RQ2_vulnerability_trends_by_severity.png') has been generated, comparing LOW, MEDIUM, and HIGH severity issues over time.\n\n")
        
        report.write("RQ3: Top 10 Most Frequent CWEs\n")
        report.write("-" * 50 + "\n")
        report.write("A bar chart ('RQ3_top_cwes.png') has been generated, showing the top 10 most frequent CWE identifiers.\n")
        report.write("The top CWEs are:\n")
        for cwe, freq in top_cwes:
            report.write(f"  {cwe}: {freq}\n")
    
    print(f"Overall analysis complete. Report saved to {report_output_file}")

# Example usage:
if __name__ == "__main__":
    # Update 'input_folder' to the directory containing your Bandit JSON files.
    input_folder = 'bandit_result'
    report_output_file = 'overall_analysis_report.txt'
    overall_analysis(input_folder, report_output_file)
