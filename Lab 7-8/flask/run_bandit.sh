# # #!/bin/bash

# # # Ensure we are on the main branch
# # git checkout main

# # # Read each commit hash from commit_list.txt
# # while read commit; do
# #     echo "Checking out commit $commit"
# #     git checkout $commit
    
# #     # Run bandit recursively, output in JSON format
# #     bandit -r . -f json -o bandit_output_${commit}.json
    
# #     # Optional: Extract and print summary from JSON output
# #     echo "Bandit run for commit $commit completed."
# # done < commit_list.txt

# # # Return to the main branch at the end
# # git checkout main



# #!/bin/bash

# # Ensure we are on the main branch
# git checkout main

# # Create the bandit_result directory if it doesn't exist
# mkdir -p bandit_result

# # Read each commit hash from commit_list.txt
# while read commit; do
#     echo "Checking out commit $commit"
#     git checkout $commit
    
#     # Run bandit recursively, output in JSON format, saving to the bandit_result folder
#     bandit -r . -f json -o bandit_result/bandit_output_${commit}.json
    
#     # Optional: Extract and print summary from JSON output
#     echo "Bandit run for commit $commit completed."
# done < commit_list.txt

# # Return to the main branch at the end
# git checkout main


#!/bin/bash

# Ensure we are on the main branch
git checkout main

# Create the bandit_result directory if it doesn't exist
mkdir -p bandit_result

# Read each commit hash from commit_list.txt
while read commit; do
    output_file="bandit_result/bandit_output_${commit}.json"
    
    # Check if the Bandit output file already exists
    if [[ -f "$output_file" ]]; then
        echo "Skipping commit $commit as the output file already exists: $output_file"
        continue
    fi
    
    echo "Checking out commit $commit"
    git checkout $commit
    
    # Run bandit recursively, output in JSON format, saving to the bandit_result folder
    bandit -r . -f json -o "$output_file"
    
    # Optional: Extract and print summary from JSON output
    echo "Bandit run for commit $commit completed."
done < commit_list.txt

# Return to the main branch at the end
git checkout main
