#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define BUFFER_SIZE 4096 // Read and write in 4KB chunks

int main(int argc, char *argv[]) {
    // Verify correct number of arguments
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_file> <output_file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Open input file for reading
    int input_fd = open(argv[1], O_RDONLY);
    if (input_fd == -1) {
        perror("Error opening input file");
        return EXIT_FAILURE;
    }

    // Open (or create) output file for writing
    int output_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (output_fd == -1) {
        perror("Error opening output file");
        close(input_fd);
        return EXIT_FAILURE;
    }

    // Buffer for reading and writing
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read, bytes_written;

    // Read from input file and write to output file in chunks
    while ((bytes_read = read(input_fd, buffer, BUFFER_SIZE)) > 0) {
        bytes_written = write(output_fd, buffer, bytes_read);
        if (bytes_written == -1) {
            perror("Error writing to output file");
            close(input_fd);
            close(output_fd);
            return EXIT_FAILURE;
        }
    }

    // Handle read error
    if (bytes_read == -1) {
        perror("Error reading input file");
        close(input_fd);
        close(output_fd);
        return EXIT_FAILURE;
    }

    // Close files
    if (close(input_fd) == -1) {
        perror("Error closing input file");
    }
    if (close(output_fd) == -1) {
        perror("Error closing output file");
    }

    printf("File copied successfully from '%s' to '%s'.\n", argv[1], argv[2]);
    return EXIT_SUCCESS;
}

