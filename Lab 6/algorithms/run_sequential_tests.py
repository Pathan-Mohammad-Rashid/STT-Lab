import subprocess
import re

def run_pytest_once():
    """
    Runs pytest with given options and returns the extracted run time (in seconds).
    Assumes that pytest's summary line contains a substring like 'in X.XXs'.
    """
    # Run pytest and capture output (stdout and stderr)
    result = subprocess.run(
        ["pytest", "--maxfail=1", "--disable-warnings"],
        capture_output=True, text=True
    )
    output = result.stdout + "\n" + result.stderr

    # Use regex to find the execution time in the output (e.g., 'in 2.05s')
    match = re.search(r'in\s+([\d\.]+)s', output)
    if match:
        run_time = float(match.group(1))
        return run_time, output
    else:
        return None, output

def main():
    num_runs = 3
    total_time = 0.0

    for i in range(1, num_runs + 1):
        print(f"Sequential Run {i}")
        run_time, output = run_pytest_once()
        if run_time is not None:
            print(f"Run time: {run_time:.2f} seconds\n")
            total_time += run_time
        else:
            print("Run time not found in the output. Please check the pytest output for details.\n")
    
    average_time = total_time / num_runs
    print(f"Average sequential time (T_seq): {average_time:.2f} seconds")

if __name__ == '__main__':
    main()
