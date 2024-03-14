#!/bin/bash

# Configuration
DB_HOST="localhost"
BACKUP_DIR="./backup_folder"
RETENTION_PERIOD_DAYS=1

# Function to backup MySQL database
backup_mysql() {
    local backup_file="$BACKUP_DIR/${DB_NAME}_$(date +"%Y%m%d_%H%M").sql"
    mysqldump -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$backup_file"
}

# Function to backup PostgreSQL database
backup_postgresql() {
    local backup_file="$BACKUP_DIR/${DB_NAME}_$(date +"%Y%m%d_%H%M").sql"
    pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" "$DB_NAME" > "$backup_file"
}

# Prompt for database type
read -p "mysql or postgresql: " DB_TYPE

# Prompt for database username
read -p "DB username: " DB_USER

# Prompt for database password
read -s -p "DB password: " DB_PASS
echo

# Prompt for database port
read -p "DB port (leave blank for default): " DB_PORT

if [ -z "$DB_PORT" ] #If string is empty
then
    case "$DB_TYPE" in
        "mysql")
            DB_PORT="3302"
            ;;
        *)
            DB_PORT="5432"
            ;;
    esac
fi

# Check if backup directory exists, if not create it
if [ ! -d "$BACKUP_DIR" ]
then
    mkdir -p "$BACKUP_DIR"
fi

# Execute backup based on database type
case "$DB_TYPE" in
    "mysql")
        # Fetch MySQL databases
        echo "Fetching MySQL databases..."
        mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p"$DB_PASS" -e "SHOW DATABASES;" | grep -Ev "Database|information_schema|performance_schema|sys" > /tmp/mysql_databases.txt || { echo "Error: Failed to fetch MySQL databases"; exit 1; }
        echo "Available MySQL databases:"
        cat /tmp/mysql_databases.txt
        echo "Enter the name of the MySQL database you want to backup:"
        read selected_database
        DB_NAME=$selected_database
        backup_mysql
        ;;
    "postgresql")
        # Fetch PostgreSQL databases
        echo "Fetching PostgreSQL databases..."
        psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -t -c "SELECT datname FROM pg_database WHERE datistemplate = false;" | grep -v "^postgres$" > /tmp/postgresql_databases.txt || { echo "Error: Failed to fetch PostgreSQL databases"; exit 1; }
        echo "Available PostgreSQL databases:"
        cat /tmp/postgresql_databases.txt
        echo "Enter the name of the PostgreSQL database you want to backup:"
        read selected_database
        DB_NAME=$selected_database
        backup_postgresql
        ;;
    *)
        echo "Error: Unsupported database type"
        exit 1
        ;;
esac

# Remove old backups
echo "Removing backups older than ${RETENTION_PERIOD_DAYS} days. "
find "$BACKUP_DIR" -type f -name "*.sql" -mtime +$RETENTION_PERIOD_DAYS -exec rm {} \;
