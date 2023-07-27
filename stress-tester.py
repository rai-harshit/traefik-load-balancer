import subprocess
import numpy as np
import logging
import re

# Function to run the provided script and return the response times
def run_script_once():
    process = subprocess.Popen(["python3", "test_endpoints.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    # Combine stdout and stderr to capture all output
    output = stdout + stderr
    # print(output)
    # Extract response times from the logs using regular expression
    response_times = [float(time) for time in re.findall(r"Response time: (\d+\.\d+)", output)]
    return response_times

# Function to run the provided script multiple times and aggregate the results
def run_script_multiple_times(total_runs):
    all_response_times = []

    for i in range(total_runs):
        print(f"Running iteration {i+1}/{total_runs}...")
        response_times = run_script_once()
        all_response_times.extend(response_times)

    return all_response_times

def main():
    total_runs = 50

    logging.info("Running the script 1000 times...")

    response_times = run_script_multiple_times(total_runs)

    # Calculate overall statistics
    average_response_time = np.mean(response_times)
    max_response_time = np.max(response_times)
    min_response_time = np.min(response_times)
    percentile_10th = np.percentile(response_times, 10)
    percentile_25th = np.percentile(response_times, 25)
    percentile_75th = np.percentile(response_times, 75)
    percentile_90th = np.percentile(response_times, 90)
    percentile_99th = np.percentile(response_times, 99)

    print("========== Overall Statistics ==========")
    print(f"Total Runs: {total_runs}")
    print(f"Average Response Time: {average_response_time:.2f} seconds")
    print(f"Maximum Response Time: {max_response_time:.2f} seconds")
    print(f"Minimum Response Time: {min_response_time:.2f} seconds")
    print(f"10th Percentile Response Time: {percentile_10th:.2f} seconds")
    print(f"25th Percentile Response Time: {percentile_25th:.2f} seconds")
    print(f"75th Percentile Response Time: {percentile_75th:.2f} seconds")
    print(f"90th Percentile Response Time: {percentile_90th:.2f} seconds")
    print(f"99th Percentile Response Time: {percentile_99th:.2f} seconds")
    

if __name__ == "__main__":
    main()
