#include<stdio.h>
void enqueue();
void display();
void dequeue();
#define MAX 10
int FRONT=-1,REAR=-1;
int arr[MAX];

int main()
{
    int option;
    do
    {
        printf("\n1. INSERT");
        printf("\n2. DISPLAY");
        printf("\n3. DELETE");
        printf("\n4. EXIT");
        printf("\n\nEnter your option: ");
        scanf("%d",&option);
        switch(option)
        {
            case 1:
                enqueue();
                break;
            case 2:
                display();
                break;
            case 3:
                dequeue();
                break;
        }
    }while(option!=4);
}

void enqueue()
{
    //int max=sizeof(arr) / sizeof(arr[0]);
    int data;
    printf("\nInsert element in queue: ");
    scanf("%d",&data);
    if(REAR==MAX-1)
    {
        printf("\nQueue is overflowed\n");
    }
    else if(FRONT ==-1 && REAR==-1)
    {
        FRONT=REAR=0;
    }
    arr[REAR]=data;
    REAR++;
    
}

void display()
{
   int i;
   if(arr[FRONT]==0)
   {
    printf("Queue is empty");
   }
   else
   {
        printf("Elements in queue are: ");
        for(i=FRONT;i<REAR;i++)
        {
            printf("\n%d",arr[i]);
        }
   }
}

void dequeue()
{
    int i;
    if(REAR ==-1 && FRONT ==-1)
    {
        printf("Queue is underflown");
    }
    else
    {
        printf("\n%d is deleted\n",arr[FRONT]);
        FRONT++;
    }
}