#include <stdio.h>
#include <stdlib.h>

struct node
{
    char c;
    struct node *next;
};

int main()
{
    struct node *head = NULL, *p = NULL;
    head = (struct node *)malloc(sizeof(struct node));
    head->c = 'a';
    head->next = (struct node *)malloc(sizeof(struct node));
    head->next->c = 'b';
    head->next->next = (struct node *)malloc(sizeof(struct node));
    head->next->next->c = 'c';
    head->next->next->next = (struct node *)malloc(sizeof(struct node));
    head->next->next->next->c = 'd';
    head->next->next->next->next = (struct node *)malloc(sizeof(struct node));
    head->next->next->next->next->c = 'e';
    head->next->next->next->next->next = (struct node *)malloc(sizeof(struct node));
    head->next->next->next->next->next->c = 'f';
    head->next->next->next->next->next->next = NULL;

    p = head->next->next;
    p->next->next->next = p;
    head->next = p->next;
    printf("%c\n", head->next->next->next->next->c);
    free(head);
    return 0;
}