#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>

int main(){
	struct stat st;
	stat("sample.txt",&st);
	printf("info about original file\n");
	printf("size of file %lld\n", st.st_size);
	printf("inode file %lld", st.st_ino);
	mode_t mode=st.st_mode;
	if(S_ISREG(mode)){
		printf("regular file\n");
	}
	if(S_ISLNK(mode)){
		printf("symbolic link\n");
	}
	return 0;
}
