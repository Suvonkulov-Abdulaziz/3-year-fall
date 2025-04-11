echo "before set: \$1=$1, \$2=$2, \$3=$3"

# using 'set' to change positional parameters
set s1 s2 s3
echo "After set: \$1=$1, \$2=$2, \$3=$3"

# using 'unset' to remove a variable
var="Hello"
echo "Before unset: var=$var"
unset var
echo "After unset: var=${var:-Unset}"

# using 'shift' to move positional parameters
shift
echo "After shift: \$1=$1, \$2=$2, \$3=$3"

