# error handling
trap 'echo "unexpected error" exit' ERR
#checking
if [ $# -ne 2]; then
	echo "Usage: $0 <filename> <pattern>"
	exit 1
fi
# check the readable or exist
if [ ! -r "$1" ]; then
	echo "Error: $1 not found or not readable"
	exit 1
fi
# searcing the pattern
grep -n "$2" "$1" || echo "No matches"   
