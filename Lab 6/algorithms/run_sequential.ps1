# Initialize an empty array to store execution times (in milliseconds)
$sequentialTimes = @()

# Run the test suite sequentially 5 times
1..5 | ForEach-Object {
    Write-Output "Sequential Run :"
    
    # Measure the time taken by pytest and capture the result
    $result = Measure-Command { pytest }
    
    # Extract the total elapsed time in milliseconds
    $ms = $result.TotalMilliseconds
    Write-Output "Run $_ took $ms milliseconds."
    
    # Append the time to the array
    $sequentialTimes += $ms
}

# Calculate the average sequential time (Tseq)
$Tseq = ($sequentialTimes | Measure-Object -Average).Average
Write-Output "Average Sequential Time (Tseq): $Tseq milliseconds"

# Save the output to a file for documentation
$sequentialTimes | Out-File "sequential_times.txt"
"Average Sequential Time (Tseq): $Tseq milliseconds" | Out-File "sequential_summary.txt" -Append
