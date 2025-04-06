total_time=0
for i in {1..3}; do
    echo "Sequential Run $i"
    output=$(pytest --maxfail=1 --disable-warnings)
    # Extract time using grep and awk (example assuming output includes "in X.XXs")
    run_time=$(echo "$output" | grep -oP 'in \K[\d\.]+(?=s)')
    echo "Run time: $run_time seconds"
    total_time=$(echo "$total_time + $run_time" | bc)
done

T_seq=$(echo "scale=2; $total_time / 3" | bc)
echo "Average sequential time (T_seq): $T_seq seconds"
