#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
int main(){
	int fd = open("sample.txt", O_RDONLY);
	char buffer[10];
	ssize_t bytes_read;
	
	if (fd==-1){
		perror("open");
		return -1;
	}	
	int pos_bytes = lseek(fd,5,SEEK_SET);
	printf("lseek %d\n", pos_bytes);
	
	if(read(fd,buffer,10)==-1){
		perror("read");
		return -1;
	}	
	
	printf("readed data %s\n", buffer);
	return 0;
}
