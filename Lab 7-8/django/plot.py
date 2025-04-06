import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file generated from bandit scans
df = pd.read_csv('aggregated_bandit_results.csv')

# Example Plot: Vulnerability Severity over Commits
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['high_severity'], label='High Severity', marker='o')
plt.plot(df.index, df['medium_severity'], label='Medium Severity', marker='o')
plt.plot(df.index, df['low_severity'], label='Low Severity', marker='o')
plt.xlabel('Commit Index (Timeline)')
plt.ylabel('Number of Vulnerabilities')
plt.title('Vulnerability Severity Trend Over Last 100 Commits')
plt.legend()
plt.grid(True)
plt.savefig('severity_trend.png')
plt.show()

# Example: Count of unique CWEs across commits
def extract_cwes(cwe_str):
    return cwe_str.split(';') if pd.notnull(cwe_str) and cwe_str != "" else []

df['cwe_list'] = df['unique_cwes'].apply(extract_cwes)
all_cwes = df['cwe_list'].sum()  # Flatten list
cwe_series = pd.Series(all_cwes)
cwe_counts = cwe_series.value_counts()

plt.figure(figsize=(10, 5))
cwe_counts.plot(kind='bar')
plt.xlabel('CWE')
plt.ylabel('Frequency')
plt.title('Frequency of Unique CWEs across Commits')
plt.tight_layout()
plt.savefig('cwe_frequency.png')
plt.show()
