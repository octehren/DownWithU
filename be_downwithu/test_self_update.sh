#!/bin/bash
pip freeze > backup_requirements.txt
echo -e "\nMaking sure all dependencies and test dependencies are present...\n\n"
pip install -r requirements_test.txt
echo -e "\n\nUninstalling yt-dlp's current version...\n\n"
pip uninstall yt-dlp -y
echo -e "\n\nInstalling an outdated yt-dlp version...\n\n"
pip install yt-dlp===2021.11.10


# Run self_update.sh, initial test will fail due to outdate yt-dlp, should update to a working version
# Running it into a subshell (the parenthesis) so its exit code won't terminate this script.
( 
  source ./self_update.sh
)
echo "\n\nCool, self update should have been successful!\n\n\nUninstalling yt-dlp..."
pip freeze | xargs pip uninstall -y
echo "...and restoring original yt-dlp version."
# this should be created in self_update.sh; since this is only a test, we'll delete and restore from backup.
rm requirements.txt && mv backup_requirements.txt requirements.txt
pip install -r requirements.txt