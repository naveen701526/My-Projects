#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int i;
    struct node *next;
} Node;

int main()
{
    Node *head = NULL, *t = NULL, *temp = NULL, *p, *d; //\*d
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
    // condition checking for zero nodes in a linked list
    // if (head == NULL)
    // {
    //     printf("there are zero nodes");
    // }

    // conditon checking for one node present in a linked list
    // if (head->next == NULL)
    // {
    //     free(head);
    // head = NULL;
    // }

    // deleting a node in a linked list
    // temp = head;
    // head = head->next;
    // free(temp);

    // deleting a node at the end or tail
    // temp = head;
    // while (temp->next->next)
    // {
    //     temp = temp->next;
    // }
    // t = temp;
    // t = t->next;
    // temp->next = NULL;
    // free(t);

    // deleting a node at a specific position

    // temp = head;
    // while (temp->i != 2)
    // {
    //     temp = temp->next;
    // }
    // t = temp;
    // d = t->next;
    // t->next = t->next->next;

    // p = head;
    // printf("\n");
    // while (p)
    // {
    //     printf("%d\n", p->i);
    //     p = p->next;
    // }

    return 0;
}
