#save directory in dir, by defolt currect directory
DIR=${1:-.} 
echo "Searching file in $DIR"

#using find to get file from directory

for file in $(find "$DIR" -type f); do
    echo "Found file: $file"
done
