#include <stdio.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    // if (!file) { perror("fopen"); return 1; }

    int c;
    while (
        (c = fgetc(file)) != EOF
    ) {
        fputc(c, stdout);
    }

    fclose(file);
}