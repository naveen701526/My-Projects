#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int i;
    struct node *next;
} Node;

Node *linear_list(Node *, int);

int main()
{
    Node *head = NULL, *t = NULL;
    int n, target;
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
    printf("enter the target number : ");
    scanf("%d", &target);
    printf("the number is at %u\n", linear_list(head, target));
    return 0;
}

Node *linear_list(Node *head, int target)
{
    if (head)
    {
        while (head)
        {
            if (head->i == target)
                return head;
            head = head->next;
        }
    }

    return head;
}