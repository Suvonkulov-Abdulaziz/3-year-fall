if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <name> <university> <date of birth>"
    exit 1
fi

echo "$1" > sys1
echo "$2" > sys2
echo "$3" > sys3

echo "system information:"
echo "username: $(whoami)"
echo "current date and time: $(date)"
echo "present working directory: $(pwd)"
echo "files in the current directory with permissions and inode numbers:"
ls -li

sys_count=$(ls sys* 2>/dev/null | wc -l)
echo "Total number of files starting with 'sys': $sys_count"

sys_count=0
for file in sys*; do
	if [ -f "$file" ]; then
		((sys_count++))
	fi
done
echo "file with 'sys': $sys_count"
