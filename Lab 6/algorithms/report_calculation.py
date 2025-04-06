import pandas as pd
import matplotlib.pyplot as plt

# Manually input run times (in seconds) for each configuration:
# (Change these values to match your measurements.)
sequential_times = [6.77, 5.23, 5.66]
xdist_load_times = [9.69, 8.10, 9.84]
xdist_no_times   = [10.16, 8.45, 10.90]
run_parallel_times = [42.60, 54.21, 65.80]

# Calculate average times:
T_seq = sum(sequential_times) / len(sequential_times)
T_xdist_load = sum(xdist_load_times) / len(xdist_load_times)
T_xdist_no = sum(xdist_no_times) / len(xdist_no_times)
T_run_parallel = sum(run_parallel_times) / len(run_parallel_times)

# Calculate speedup ratios (using T_seq as the baseline, so sequential speedup is 1.0):
speedup_xdist_load = T_seq / T_xdist_load if T_xdist_load else 0
speedup_xdist_no = T_seq / T_xdist_no if T_xdist_no else 0
speedup_run_parallel = T_seq / T_run_parallel if T_run_parallel else 0

# Create an execution matrix DataFrame:
data = {
    "Configuration": [
        "Sequential",
        "pytest-xdist --dist=load",
        "pytest-xdist --dist=no",
        "pytest-run-parallel (--parallel-threads=auto)"
    ],
    "Average Time (s)": [T_seq, T_xdist_load, T_xdist_no, T_run_parallel],
    "Speedup": [1.0, speedup_xdist_load, speedup_xdist_no, speedup_run_parallel]
}

df = pd.DataFrame(data)
print("Execution Matrix:")
print(df)

# Save the execution matrix to a CSV file for your report (optional):
df.to_csv("execution_matrix.csv", index=False)

# Plot the speedup ratios for parallel configurations (excluding sequential):
df_parallel = df[df["Configuration"] != "Sequential"]

plt.figure(figsize=(8, 5))
bars = plt.bar(df_parallel["Configuration"], df_parallel["Speedup"], color='skyblue')
plt.xlabel("Configuration")
plt.ylabel("Speedup (T_seq / T_par)")
plt.title("Speedup Ratios for Parallel Configurations")
plt.ylim(0, max(df_parallel["Speedup"]) + 0.5)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2.0,
        bar.get_height() + 0.05,
        f"{bar.get_height():.2f}",
        ha='center',
        va='bottom',
        fontweight='bold'
    )
plt.tight_layout()
plt.savefig("speedup_plot.png")
plt.show()
