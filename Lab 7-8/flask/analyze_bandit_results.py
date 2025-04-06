# # # import os
# # # import json
# # # import pandas as pd

# # # # Directory containing Bandit JSON output files
# # # results_dir = 'bandit_result'

# # # # Lists to store extracted data
# # # commit_hashes = []
# # # file_names = []
# # # line_numbers = []
# # # severities = []
# # # confidences = []
# # # cwe_ids = []
# # # issue_texts = []

# # # # Iterate over each JSON file in the results directory
# # # for filename in os.listdir(results_dir):
# # #     if filename.endswith('.json'):
# # #         commit_hash = filename.replace('bandit_output_', '').replace('.json', '')
# # #         file_path = os.path.join(results_dir, filename)
        
# # #         with open(file_path, 'r') as file:
# # #             data = json.load(file)
            
# # #             # Extract metrics
# # #             metrics = data.get('metrics', {})
# # #             total_high_severity = metrics.get('SEVERITY.HIGH', 0)
# # #             total_medium_severity = metrics.get('SEVERITY.MEDIUM', 0)
# # #             total_low_severity = metrics.get('SEVERITY.LOW', 0)
# # #             total_high_confidence = metrics.get('CONFIDENCE.HIGH', 0)
# # #             total_medium_confidence = metrics.get('CONFIDENCE.MEDIUM', 0)
# # #             total_low_confidence = metrics.get('CONFIDENCE.LOW', 0)
            
# # #             # Append metrics to lists
# # #             commit_hashes.append(commit_hash)
# # #             file_names.append('N/A')  # Placeholder, will update later
# # #             line_numbers.append('N/A')  # Placeholder, will update later
# # #             severities.append(f'High: {total_high_severity}, Medium: {total_medium_severity}, Low: {total_low_severity}')
# # #             confidences.append(f'High: {total_high_confidence}, Medium: {total_medium_confidence}, Low: {total_low_confidence}')
# # #             cwe_ids.append('N/A')  # Placeholder, will update later
# # #             issue_texts.append('N/A')  # Placeholder, will update later

# # #             # Extract individual issues
# # #             for result in data.get('results', []):
# # #                 file_name = result.get('filename', 'N/A')
# # #                 line_number = result.get('line_number', 'N/A')
# # #                 severity = result.get('issue_severity', 'N/A')
# # #                 confidence = result.get('issue_confidence', 'N/A')
# # #                 cwe_id = result.get('test_id', 'N/A')
# # #                 issue_text = result.get('issue_text', 'N/A')
                
# # #                 # Update lists with issue details
# # #                 file_names.append(file_name)
# # #                 line_numbers.append(line_number)
# # #                 severities.append(severity)
# # #                 confidences.append(confidence)
# # #                 cwe_ids.append(cwe_id)
# # #                 issue_texts.append(issue_text)

# # # # Create a DataFrame from the collected data
# # # df = pd.DataFrame({
# # #     'Commit Hash': commit_hashes,
# # #     'File Name': file_names,
# # #     'Line Number': line_numbers,
# # #     'Severity': severities,
# # #     'Confidence': confidences,
# # #     'CWE ID': cwe_ids,
# # #     'Issue Text': issue_texts
# # # })

# # # # Save the DataFrame to a CSV file for further analysis
# # # df.to_csv('bandit_analysis_results.csv', index=False)

# # # print("Analysis complete. Results saved to 'bandit_analysis_results.csv'.")


# # import os
# # import json
# # import pandas as pd

# # # Directory containing Bandit JSON output files
# # results_dir = 'bandit_result'

# # # List to store individual issues
# # issues = []

# # # Iterate over each JSON file in the results directory
# # for filename in os.listdir(results_dir):
# #     if filename.endswith('.json'):
# #         commit_hash = filename.replace('bandit_output_', '').replace('.json', '')
# #         file_path = os.path.join(results_dir, filename)
        
# #         with open(file_path, 'r') as file:
# #             data = json.load(file)
            
# #             # Extract individual issues
# #             for result in data.get('results', []):
# #                 issue = {
# #                     'Commit Hash': commit_hash,
# #                     'File Name': result.get('filename', 'N/A'),
# #                     'Line Number': result.get('line_number', 'N/A'),
# #                     'Severity': result.get('issue_severity', 'N/A'),
# #                     'Confidence': result.get('issue_confidence', 'N/A'),
# #                     'CWE ID': result.get('test_id', 'N/A'),
# #                     'Issue Text': result.get('issue_text', 'N/A')
# #                 }
# #                 issues.append(issue)

# # # Create a DataFrame from the list of issues
# # df = pd.DataFrame(issues)

# # # Save the DataFrame to a CSV file for further analysis
# # df.to_csv('bandit_analysis_results.csv', index=False)

# # print("Analysis complete. Results saved to 'bandit_analysis_results.csv'.")


# import json
# import glob
# import os

# # Create dictionaries to store commit-level data
# commit_data = {}

# # Process each Bandit JSON output file
# for filepath in glob.glob("bandit_output_*.json"):
#     commit = os.path.basename(filepath).split('_')[-1].split('.')[0]
#     with open(filepath, 'r') as f:
#         data = json.load(f)
    
#     # Initialize counters
#     confidence_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
#     severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
#     cwe_set = set()
    
#     # Loop over each reported issue
#     for issue in data.get("results", []):
#         # Normalize and count confidence
#         conf = issue.get("issue_confidence", "").upper()
#         if conf in confidence_counts:
#             confidence_counts[conf] += 1
        
#         # Normalize and count severity
#         sev = issue.get("issue_severity", "").upper()
#         if sev in severity_counts:
#             severity_counts[sev] += 1
        
#         # Add CWE identifier if available
#         cwe = issue.get("cwe")
#         if cwe:
#             cwe_set.add(cwe)
    
#     commit_data[commit] = {
#         "confidence": confidence_counts,
#         "severity": severity_counts,
#         "unique_cwes": list(cwe_set)
#     }

# # Print results for each commit
# for commit, results in commit_data.items():
#     print(f"Commit: {commit}")
#     print(f"  Confidence counts: {results['confidence']}")
#     print(f"  Severity counts:   {results['severity']}")
#     print(f"  Unique CWEs:       {results['unique_cwes']}")
#     print("--------------------------------------------------")





import os
import json
from collections import defaultdict

def analyze_bandit_reports(input_folder, output_file):
    # Initialize dictionaries to store aggregated counts
    confidence_counts = defaultdict(int)
    severity_counts = defaultdict(int)
    unique_cwes = set()
    commit_data = []

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                commit_hash = filename.replace('bandit_output_', '').replace('.json', '')

                # Initialize counts for the current commit
                commit_confidence_counts = defaultdict(int)
                commit_severity_counts = defaultdict(int)
                commit_cwes = set()

                # Process each issue in the report
                for result in data.get('results', []):
                    confidence = result.get('issue_confidence', 'UNKNOWN')
                    severity = result.get('issue_severity', 'UNKNOWN')
                    cwe = result.get('cwe', 'UNKNOWN')

                    # Update commit-specific counts
                    commit_confidence_counts[confidence] += 1
                    commit_severity_counts[severity] += 1
                    if cwe != 'UNKNOWN':
                        commit_cwes.add(cwe)

                    # Update overall counts
                    confidence_counts[confidence] += 1
                    severity_counts[severity] += 1
                    if cwe != 'UNKNOWN':
                        unique_cwes.add(cwe)

                # Store commit-specific data
                commit_data.append({
                    'commit': commit_hash,
                    'confidence_counts': dict(commit_confidence_counts),
                    'severity_counts': dict(commit_severity_counts),
                    'unique_cwes': list(commit_cwes)
                })

    # Write aggregated results to the output file
    with open(output_file, 'w') as out_file:
        out_file.write("Aggregated Bandit Analysis Report\n")
        out_file.write("="*40 + "\n\n")
        out_file.write("Overall Confidence Counts:\n")
        for confidence, count in confidence_counts.items():
            out_file.write(f"  {confidence}: {count}\n")
        out_file.write("\nOverall Severity Counts:\n")
        for severity, count in severity_counts.items():
            out_file.write(f"  {severity}: {count}\n")
        out_file.write("\nUnique CWEs Identified:\n")
        for cwe in unique_cwes:
            out_file.write(f"  {cwe}\n")
        out_file.write("\nDetailed Commit Analysis:\n")
        for commit in commit_data:
            out_file.write(f"\nCommit: {commit['commit']}\n")
            out_file.write("  Confidence Counts:\n")
            for confidence, count in commit['confidence_counts'].items():
                out_file.write(f"    {confidence}: {count}\n")
            out_file.write("  Severity Counts:\n")
            for severity, count in commit['severity_counts'].items():
                out_file.write(f"    {severity}: {count}\n")
            out_file.write("  Unique CWEs:\n")
            for cwe in commit['unique_cwes']:
                out_file.write(f"    {cwe}\n")

# Example usage:
input_folder = 'bandit_result'
output_file = 'bandit_analysis_report.txt'
analyze_bandit_reports(input_folder, output_file)
