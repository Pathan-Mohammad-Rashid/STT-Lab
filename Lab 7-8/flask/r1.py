import subprocess
import datetime
import matplotlib.pyplot as plt

# List to store commit dates and corresponding high severity count
commit_dates = []
high_severity_counts = []

for commit in commit_data.keys():
    # Get commit date using git log
    result = subprocess.run(["git", "show", "-s", "--format=%ci", commit],
                            capture_output=True, text=True)
    date_str = result.stdout.strip()  # e.g., "2024-05-01 12:34:56 +0000"
    commit_date = datetime.datetime.strptime(date_str.split(' ')[0], "%Y-%m-%d")
    commit_dates.append(commit_date)
    
    # Get count of high severity issues
    high_count = commit_data[commit]['severity'].get("HIGH", 0)
    high_severity_counts.append(high_count)

# Sort the data by date
dates, counts = zip(*sorted(zip(commit_dates, high_severity_counts)))

# Plot the timeline
plt.figure(figsize=(10, 5))
plt.plot(dates, counts, marker='o')
plt.title("High Severity Vulnerabilities Over Time")
plt.xlabel("Commit Date")
plt.ylabel("Number of High Severity Issues")
plt.grid(True)
plt.show()
