#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    // открываем файл
    int file_descriptor = open("input.txt", O_RDONLY);

    char buffer[256];
    ssize_t n;

    while (
        (n = read(file_descriptor, buffer, sizeof(buffer))) > 0
    ) {
        write(STDOUT_FILENO, buffer, n);
    }

    close(file_descriptor);
}