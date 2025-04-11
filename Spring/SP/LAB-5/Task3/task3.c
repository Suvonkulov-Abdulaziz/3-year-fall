#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    int file = open("example.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (file == -1) {
        perror("Error opening file");
        return -1;
    }

    size_t bytes_written = write(file, "Hello, this is a test message", 29);
    if (bytes_written == -1) {
        perror("Error writing to file");
        close(file);
        return EXIT_FAILURE;
    }

    if (close(file) == -1) {
        perror("Error closing file");
        return -1;
    }

    printf("File 'example.txt' created and message written successfully.\n");
    return 0;
}

