#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main(void) {
    int fdsc = open("text.txt", O_RDONLY);
    // if (fdsc < 0) { perror("open"); return 1; }

    lseek(fdsc, 3, SEEK_SET);

    char buf[5];
    ssize_t n = read(fdsc, buf, 5);
    // if (n < 0) { perror("read"); return 1; }

    write(STDOUT_FILENO, buf, n);
    write(STDOUT_FILENO, "\n", 1);

    close(fdsc);
}