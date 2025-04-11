
# directory to monitor
monitor_dir="."

# notify when a new file is added 
#installed fswatch for notification
fswatch -0 "$monitor_dir" | while read -d "" new_file; do
    echo "New file added: $new_file"
done

