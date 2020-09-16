#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int i;
    struct node *next;
} Node;

int main()
{
    Node *head = NULL, *t = NULL, *temp = NULL;
    int n;
    scanf("%d", &n);
    head = (Node *)malloc(sizeof(Node));
    scanf("%d", &head->i);
    t = head;
    while (n > 1)
    {
        t->next = (Node *)malloc(sizeof(Node));

        t = t->next;
        scanf("%d", &t->i);
        n--;
    }
    t->next = NULL;
    temp = head;
    while (temp)
    {
        printf("%d\n", temp->i);
        temp = temp->next;
    }
    return 0;
}