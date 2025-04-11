#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(){
	printf("starting PID =%d\n", getpid());
	pid_t pid = fork();
	if(pid == 0){
		sleep(0);
:wq
	}
}
