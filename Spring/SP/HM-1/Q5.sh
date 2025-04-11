
[ $# -ne 2 ] && echo "usage: $0 <num1> <num2>" && exit 1

num1=$1
num2=$2

echo "sum: $(expr $num1 + $num2)"
echo "difference: $(expr $num1 - $num2)"
echo "product: $(expr $num1 \* $num2)"

if [ $num2 -ne 0 ]; then
    quotient=$(expr $num1 / $num2)
else
    quotient="Not divisible"
fi

echo "Division: $quotient"

