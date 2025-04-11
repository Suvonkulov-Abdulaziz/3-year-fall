#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]){
	printf("get PID= %d\n", getpid());
	execlp("ps","ps","ax", (char *)NULL);
	return 0;
}
