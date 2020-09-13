#include<stdio.h>

int main(){
    int num;
    // Take the number as an input from the user
    printf("Enter the value of number whose multiplication table is to be printed\n");
    scanf("%d", &num);
    printf("The multiplication table of %d is\n", num);
     for (int i = 1; i <= 10; i++)
     {
         printf("%d X %d = %d\n",num, i, i*num);
     }
    
    return 0;
}

