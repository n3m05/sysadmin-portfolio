# Automated Backup System

This Bash script automates the backup of directories, keeping a retention policy to prevent disk overuse.

## Features
- Timestamped backup archives
- Automatic cleanup of old backups
- Simple configuration for source directory and retention period
- Can be extended to cloud storage (AWS S3, Google Drive, etc.)

## Installation
```bash
git clone https://github.com/n3m05/sysadmin-portfolio.git
cd sysadmin-portfolio/projects/backup-system
chmod +x backup.sh

## Usage
./backup.sh

Optional: Automate via cron
# Run every day at 2 AM
0 2 * * * /home/user/sysadmin-portfolio/projects/backup-system/backup.sh

