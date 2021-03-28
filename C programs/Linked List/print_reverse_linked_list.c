#include <stdio.h>
#include <stdlib.h>

struct node {
   int data;
   struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;

//display the list
void reverse_linked_list(struct node *list) {
   if(list == NULL) {
      printf("[null] => ");
      return;
   }
   
   reverse_linked_list(list->next);
   printf(" %d =>",list->data);
   
}

//Create Linked List
void insertion(int data) {
   // Allocate memory for new node;
   struct node *link = (struct node*) malloc(sizeof(struct node));

   link->data = data;
   link->next = NULL;

   // If head is empty, create new list
   if(head==NULL) {
      head = link;
      return;
   }

   current = head;
   
   // move to the end of the list
   while(current->next!=NULL)
      current = current->next;

   // Insert link at the end of the list
   current->next = link; 
}

int main() {
   insertion(10);
   insertion(20);
   insertion(30);
   insertion(1);
   insertion(40);
   insertion(56); 

   reverse_linked_list(head);
   return 0;
}
