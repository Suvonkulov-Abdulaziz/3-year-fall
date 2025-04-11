#get input from user

read -p "Enter file name: " filename

#check file exits or not

if [ -f "$filename" ]; then 
	echo "file exits"
else	
	touch "$filename" && echo "file created"
fi

#for find the  path of the file
find . -name "$filename" -type f -exec ls -l {} \;

  
