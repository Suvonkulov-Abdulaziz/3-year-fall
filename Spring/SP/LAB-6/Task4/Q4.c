#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    struct stat st;
    char buffer[200];

    // Get file metadata
    if (stat("sample.txt", &st) == -1) {
        perror("Error retrieving file stats");
        return EXIT_FAILURE;
    }

    // Format file metadata into a string
    sprintf(buffer, "File Size: %lld bytes\nLast Modified: %ld\nInode Number: %lld\n",
            (long long)st.st_size, (long)st.st_mtime, (long long)st.st_ino);


    FILE *fp = fopen("metadata.txt", "w");
    if (fp == NULL) {
        perror("Error opening metadata.txt");
        return EXIT_FAILURE;
    }

    // Write metadata to file
    fprintf(fp, "%s", buffer);

   
    fclose(fp);

    printf("File metadata written to metadata.txt successfully.\n");
    return EXIT_SUCCESS;
}

