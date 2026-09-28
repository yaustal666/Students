#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

static void copy_once(void) {
    int in  = open("from.txt", O_RDONLY);
    int out = open("to.txt", O_WRONLY);
    char buf[4096];
    ssize_t n;
    while ((n = read(in, buf, sizeof(buf))) > 0)
        write(out, buf, n);
    close(in);
    close(out);
}

int main(void) {
    for (int i = 0; i < 1000; i++) copy_once();
    return 0;
}