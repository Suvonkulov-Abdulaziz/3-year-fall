#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
int main(){
	char *args[]={"ls","/home", "/bin",0};
	execv("/bin/ls", args);
	return 0;
}

