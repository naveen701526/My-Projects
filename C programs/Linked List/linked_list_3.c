#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int i;
    struct node *next;
} Node;

int main()
{
    Node *head = NULL, *t = NULL, *temp; //\*new *last *mid
    int val = 1;
    head = (Node *)malloc(sizeof(Node));
    head->i = val;
    t = head;
    while (val != 4)
    {
        t->next = (Node *)malloc(sizeof(Node));
        t = t->next;

        t->i = ++val;
    }
    t->next = NULL;
    // insertion of node at the beginning
    // new = (Node *)malloc(sizeof(Node));
    // new->i = 100;
    // new->next = head;
    // head = new;

    // insertion of node at the end
    // last = (Node *)malloc(sizeof(Node));
    // last->i = 200;
    // last->next = NULL;

    // t = head;
    // while (t->next)
    //     t = t->next;

    // t->next = last;

    // insertion of node after the node you want or at a specific place in the list
    // mid = (Node *)malloc(sizeof(Node));
    // mid->i = 400;
    // mid->next = NULL;
    // t = head;
    // t = t->next;
    // mid->next = t->next;
    // t->next = mid;

    return 0;
}