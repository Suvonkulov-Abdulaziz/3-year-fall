
printenv

while true
do
	echo -e "Enter to search: "
	read env

	echo "${!env}"

done
