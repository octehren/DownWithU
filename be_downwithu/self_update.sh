#!/bin/bash

# Define the function
run_tests() {
    local retry_count=${1:-0} # starts at 0
    # Run pytest and capture the exit code
    echo -e "\n\nRunning tests...\n\n"
    pytest tests/
    TEST_RESULT=$?

    # 0 = test pass, else = test fail
    if [ $TEST_RESULT -eq 0 ]; then
        echo "All tests passed successfully!"
        echo "Working version for yt-dlp:"
        pip show yt-dlp
        exit 0  # Success
    else
        echo -e "\n\nSome tests failed. Please check the output above for details.\n\n"
        if [ $retry_count -eq 0 ]; then
          echo -e "\n\nIt seems like this version of yt-dlp does not work.\n\n"
          pip uninstall yt-dlp -y
          echo -e "\n\nAttempting to install stable build...\n\n"
          pip install yt-dlp
        elif [ $retry_count -eq 0 ]; then
          echo -e "\n\nStable build did not work. Uninstalling...\n\n"
          pip uninstall yt-dlp -y
          echo -e "\n\nWill attempt to use nightly build now.\n\n"
          pip install -U --pre "yt-dlp[default]"
        else
            echo -e "\n\n\n\nAttempted to install stable and nightly builds, none worked :( \n\n"
            echo "Double-check your environment, see if you have FFMPEG installed or wait for a new version of yt-dlp to be released."
            exit 1  # Failure
        fi
        run_tests $((retry_count + 1))
    fi
}

# Call the function
run_tests