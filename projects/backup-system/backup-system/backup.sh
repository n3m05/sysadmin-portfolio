#!/bin/bash
# Automated Backup Script
# Usage: ./backup.sh

# Configuration
SOURCE_DIR="/home/user/data"
BACKUP_DIR="/home/user/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
RETENTION_DAYS=7

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Perform backup
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" "$SOURCE_DIR"

# Remove backups older than retention period
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +$RETENTION_DAYS -exec rm {} \;

echo "Backup completed: $BACKUP_DIR/backup_$DATE.tar.gz"
