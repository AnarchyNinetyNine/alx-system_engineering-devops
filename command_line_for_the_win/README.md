# Command Line Challenge - Command Line for the Win

This repository contains screenshots of completed levels for the "Command Line for the Win" challenge.

## Task Overview

### Task 0: First Nine Tasks
To complete this task, the first 9 tasks of the challenge were finished. The screenshots for these tasks are stored in the following files:
- `0-first_9_tasks.jpg`
- `0-first_9_tasks.png`

### Task 1: Next Nine Tasks (Tasks 10-18)
The subsequent 9 tasks (tasks 10 to 18) were completed for this task. The associated screenshots are saved in the following files:
- `1-next_9_tasks.jpg`
- `1-next_9_tasks.png`

### Task 2: Achieve 27 Tasks (Tasks 19-27)
For this task, the final 9 tasks (tasks 19 to 27) were successfully completed. The respective screenshots are available in these files:
- `2-next_9_tasks.jpg`
- `2-next_9_tasks.png`

## Uploading Screenshots

The screenshots were uploaded to a sandbox environment and subsequently pushed to this GitHub repository using the following steps:

1. **Establishing Connection to Sandbox via SFTP**:
   - Opened a terminal/command prompt.
      - Used SFTP command-line tool to connect to the sandbox environment using provided credentials.

2. **Navigating and Uploading**:
   - Navigated to the directory where the screenshots were located on the local machine.
      - Used `put` command in SFTP to upload screenshots to the specified directory on the sandbox environment.

3. **Confirmation and Git Push**:
   - Confirmed successful transfer by checking the sandbox directory.
      - After transferring screenshots, utilized SSH to access the sandbox environment.
         - Added the uploaded files to the Git repository, committed changes, and pushed to GitHub.

## SFTP Command Usage

To perform the file transfer using SFTP, the following commands were used within the terminal:

```bash
# Connect to sandbox environment via SFTP
sftp username@hostname

# Navigate to the desired directory on the sandbox
cd /root/alx-system_engineering-devops/command_line_for_the_win/

# Navigate to the local directory containing screenshots
lcd /path/to/local/screenshots/directory/

# Upload screenshots to sandbox directory
put 0-first_9_tasks.jpg
put 0-first_9_tasks.png
put 1-next_9_tasks.jpg
put 1-next_9_tasks.png
put 2-next_9_tasks.jpg
put 2-next_9_tasks.png

# Exit SFTP
exit'''
