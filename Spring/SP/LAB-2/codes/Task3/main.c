#include <stdio.h>
#include "Abdulaziz.h"

int main() {
    double A[3][3], B[3][3], C[3][3];

    printf("Enter matrix A:\n");
    YourName_Get(A);
    printf("Enter matrix B:\n");
    YourName_Get(B);

    printf("\nMatrix A:\n");
    YourName_Show(A);
    printf("\nMatrix B:\n");
    YourName_Show(B);

    YourName_Add(A, B, C);
    printf("\nSum of A and B:\n");
    YourName_Show(C);

    YourName_Mul(A, B, C);
    printf("\nMultiplication of A and B:\n");
    YourName_Show(C);

    printf("\nDeterminant of A: %.2lf\n", YourName_Mod(A));

    if (YourName_Mod(A) != 0) {
        YourName_Inv(A, C);
        printf("\nInverse of A:\n");
        YourName_Show(C);
    } else {
        printf("\nMatrix A has no inverse.\n");
    }

    return 0;
}

