#get input from user

read -p "enter mathmatical expressin" exp

#evaluate using $(())

echo "result with (( )):  $((exp))"

#evaluate using expr

if result=$(expr $exp 2>/dev/null); then
	echo "result expr: $result"
else
	echo "invalid format, plese write like this '2 + 3'"
fi

