#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct phonebook_entry {
    char *name, *phone;
};

int compare_strings(const void *lhs, const void *rhs) {
    return strcmp(*((const char **) lhs), *((const char **) rhs));
}

int main() {
    // Caveat: no input validation,
    // This program relies on a POSIX-2013 extension ('m') for
    // allocating memory in scanf (see http://pubs.opengroup.org/
    // onlinepubs/9699919799.2013edition/functions/scanf.html).

    int n;
    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "could not read 'n'\n");
        exit(1);
    }

    // read the names and phone numbers
    struct phonebook_entry entries[n];
    for (int i = 0; i < n; ++i)
        if (scanf("%ms %ms", &entries[i].name, &entries[i].phone) != 2) {
            fprintf(stderr, "could not read phonebook entry #%d\n", i);
            exit(1);
        }

    // sort for binary search
    qsort(entries, n, sizeof(*entries), compare_strings);

    // read names from stdin and look them up
    char *name;
    while (scanf("%ms", &name) == 1) {
        const struct phonebook_entry *found = bsearch(
            &name, entries, n, sizeof(*entries), compare_strings);
        if (found)
            printf("%s=%s\n", found->name, found->phone);
        else
            printf("Not found\n");
        free(name);
    }

    // free all allocated memory
    for (int i = 0; i < n; ++i) {
        free(entries[i].phone);
        free(entries[i].name);
    }
}

