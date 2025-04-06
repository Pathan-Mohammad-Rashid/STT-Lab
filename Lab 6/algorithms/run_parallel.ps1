# Initialize an empty array to store parallel execution times (in milliseconds)
$parallelTimes = @()

# Define the parallel command options
$parallelOptions = "-n 4 --dist load --parallel-threads 4"

# Run the parallel test suite 5 times
1..5 | ForEach-Object {
    Write-Output "Parallel Run $_ with options ${parallelOptions}:"
    
    # Measure the time taken by pytest with parallel options
    $result = Measure-Command { pytest $parallelOptions }
    
    # Extract the total elapsed time in milliseconds
    $ms = $result.TotalMilliseconds
    Write-Output "Parallel Run $_ took $ms milliseconds."
    
    # Append the time to the array
    $parallelTimes += $ms
}

# Calculate the average parallel time (Tpar)
$Tpar = ($parallelTimes | Measure-Object -Average).Average
Write-Output "Average Parallel Time (Tpar): $Tpar milliseconds"

# Save the output to a file for documentation
$parallelTimes | Out-File "parallel_times.txt"
"Average Parallel Time (Tpar): $Tpar milliseconds" | Out-File "parallel_summary.txt" -Append
