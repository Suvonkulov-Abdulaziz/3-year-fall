#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

int main() {
    pid_t pid;
    pid = fork();
    if (pid < 0) {
        printf("Fork failed\n");
        return 1;
    }
    else if (pid == 0) {
        printf("Child process created\n");
        kill(getppid(), SIGKILL);
        return 0;
    }
    else {
        printf("Parent process created\n");
        wait(NULL);
        return 0;
    }
}