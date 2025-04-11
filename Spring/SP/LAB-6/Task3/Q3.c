#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    char buffer[100];
    
    int fd = open("sample.txt", O_RDONLY);
    if (fd == -1) {
        perror("Error opening sample.txt");
        return EXIT_FAILURE;
    }

    
    int new_fd = dup(fd);
    if (new_fd == -1) {
        perror("Error duplicating file descriptor");
        close(fd);
        return EXIT_FAILURE;
    }

    // Read from the duplicated descriptor
    ssize_t bytes_read = read(new_fd, buffer, sizeof(buffer) - 1);
    if (bytes_read == -1) {
        perror("Error reading file");
        close(fd);
        close(new_fd);
        return EXIT_FAILURE;
    }

    buffer[bytes_read] = '\0';
    printf("Read content from sample.txt:\n%s\n", buffer);

    int fd_out = open("output1.txt", O_WRONLY | O_CREAT | O_TRUNC, 0666);
    if (fd_out == -1) {
        perror("Error opening output1.txt");
        close(fd);
        close(new_fd);
        return EXIT_FAILURE;
    }

    // Redirect stdout (file descriptor 1) to output1.txt
    if (dup2(fd_out, STDOUT_FILENO) == -1) {
        perror("Error redirecting stdout");
        close(fd);
        close(new_fd);
        close(fd_out);
        return EXIT_FAILURE;
    }

    printf("This message is redirected to output1.txt using dup2.\n");

    close(fd);
    close(new_fd);
    close(fd_out);

    return EXIT_SUCCESS;
}

