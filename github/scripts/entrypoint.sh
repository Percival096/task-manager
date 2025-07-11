#!/bin/sh

# Run todo.py and save its output
python3 todo.py > task-output.txt

# Run todo-test.py and save test results
python3 todo-test.py > test-output.txt

# Run the index updater script using both outputs
bash github/scripts/update_index.sh task-output.txt test-output.txt

echo "✅ Entrypoint execution completed."
