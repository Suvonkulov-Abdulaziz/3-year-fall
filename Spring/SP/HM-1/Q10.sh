cut -d: -f1 /etc/passwd | sort
# cut extracts specific fields from a file.
# -d: sets : as the delimiter since /etc/passwd uses colons.
# -f1 selects the first field, which contains usernames.
# sort arranges them in alphabetical order.
