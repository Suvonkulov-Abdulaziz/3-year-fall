#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
	int file;
	char buffer[1024];
	ssize_t bytesRead;

	file = open("sample.txt", O_RDONLY);	
	if (file == -1){
		perror("error open file");
		return -1;
	}
	printf("success opening file %d\n", file );
	
	int nread = read(file,buffer,1024);
	write(1,buffer,nread);
	
}	
