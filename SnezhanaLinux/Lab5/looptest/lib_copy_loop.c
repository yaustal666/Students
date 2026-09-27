#include <stdio.h>

static void copy_once(void) {
    FILE *in  = fopen("from.txt", "rb");
    FILE *out = fopen("to.txt", "wb");
    char buf[4096];
    size_t n;
    while ((n = fread(buf, 1, sizeof(buf), in)) > 0)
        fwrite(buf, 1, n, out);
    fclose(in);
    fclose(out);
}

int main(void) {
    for (int i = 0; i < 1000; i++) copy_once();
    return 0;
}