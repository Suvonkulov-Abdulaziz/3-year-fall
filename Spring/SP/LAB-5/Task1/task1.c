#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	int file;
	file = open("sample.txt", O_RDONLY);
	if (file == -1){
		perror("error" );
		exit(1);
	}
	exit(0);
			
}
