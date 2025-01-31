#!/bin/bash
echo -e "\nMaking sure all dependencies and test dependencies are present...\n\n"
pip install -r requirements_test.txt
echo -e "\n\nUninstalling yt-dlp's current version...\n\n"
pip uninstall yt-dlp -y
echo -e "\n\nInstalling an outdated yt-dlp version...\n\n"
pip install yt-dlp===2021.11.10


# Run self_update.sh, initial test will fail due to outdate yt-dlp, should update to a working version
source ./self_update.sh

echo "Uninstalling yt-dlp..."
pip uninstall yt-dlp -y
echo "...and restoring original yt-dlp version."
pip install -r requirements.txt -y