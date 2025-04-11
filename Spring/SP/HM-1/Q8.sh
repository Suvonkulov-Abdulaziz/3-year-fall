# create a direction
backup_dir="backup"
mkdir -p "$backup_dir"

# get current timestamp
timestamp=$(date -u +"%Y%m%d%H%M%S")

# backup all .txt files in the current directory
for file in *.txt; do
    if [ -f "$file" ]; then
        cp "$file" "$backup_dir/${file%.*}_$timestamp.txt"
        echo "Backup created: $backup_dir/${file%.*}_$timestamp.txt"
    fi
done

echo "done"

