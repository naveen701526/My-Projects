#include <stdio.h>

#define MAXROW 10
#define MAXCOL 10

/*User Define Function to Read Matrix*/
void readMatrix(int m[][MAXCOL], int row, int col)
{
    int i, j;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("Enter element [%d,%d] : ", i + 1, j + 1);
            scanf("%d", &m[i][j]);
        }
    }
}

/*User Define Function to Read Matrix*/
void printMatrix(int m[][MAXCOL], int row, int col)
{
    int i, j;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            printf("%d\t", m[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int a[MAXROW][MAXCOL], b[MAXROW][MAXCOL], result[MAXROW][MAXCOL];
    int i, j, r1, c1, r2, c2;
    int sum, k;

    printf("Enter number of Rows of matrix a: ");
    scanf("%d", &r1);
    printf("Enter number of Cols of matrix a: ");
    scanf("%d", &c1);

    printf("\nEnter elements of matrix a: \n");
    readMatrix(a, r1, c1);

    printf("Enter number of Rows of matrix b: ");
    scanf("%d", &r2);
    printf("Enter number of Cols of matrix b: ");
    scanf("%d", &c2);

    printf("\nEnter elements of matrix b: \n");
    readMatrix(b, r2, c2);

    if (r1 == c2)
    {
        /*Multiplication of two matrices*/
        for (i = 0; i < r1; i++)
        {
            for (j = 0; j < c1; j++)
            {
                sum = 0;
                for (k = 0; k < r1; k++)
                {
                    sum = sum + (a[i][k] * b[k][j]);
                }
                result[i][j] = sum;
            }
        }

        /*print matrix*/
        printf("\nMatrix after multiplying elements (result matrix):\n");
        printMatrix(result, r1, c1);
    }
    else
    {
        printf("\nMultiplication can not be done.");
    }

    return 0;
}
