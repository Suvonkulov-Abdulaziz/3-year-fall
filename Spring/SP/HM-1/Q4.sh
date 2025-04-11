while true; do 
	echo "Enter 1 to get currect date"
	echo "Enter 2 to get currect directory"
	echo "Enter 0 to exit"
	
	read -p "Enter your choise" choise
	
	case $choise in
	1) echo "Currect date $(date)"
	;;
	2) echo "Currect directory"
	ls -l
	;;
	0) echo "GoodBye"
	exit 0
	;;
	esac
done
