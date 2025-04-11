#include <stdio.h>
#include "Abdulaziz.h"

void YourName_Get(double Mat[][3]) {
    printf("Enter 9 elements for the 3x3 matrix:\n");
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            scanf("%lf", &Mat[i][j]);
}

void YourName_Show(double Mat[][3]) {
    printf("Matrix:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            printf("%.2lf ", Mat[i][j]);
        printf("\n");
    }
}

void YourName_Add(double MatA[][3], double MatB[][3], double MatC[][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            MatC[i][j] = MatA[i][j] + MatB[i][j];
}

void YourName_Mul(double MatA[][3], double MatB[][3], double MatC[][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            MatC[i][j] = 0;
            for (int k = 0; k < 3; k++)
                MatC[i][j] += MatA[i][k] * MatB[k][j];
        }
}

double determinant(double Mat[][3]) {
    return Mat[0][0] * (Mat[1][1] * Mat[2][2] - Mat[1][2] * Mat[2][1]) -
           Mat[0][1] * (Mat[1][0] * Mat[2][2] - Mat[1][2] * Mat[2][0]) +
           Mat[0][2] * (Mat[1][0] * Mat[2][1] - Mat[1][1] * Mat[2][0]);
}

void YourName_Inv(double MatA[][3], double MatB[][3]) {
    double det = determinant(MatA);
    if (det == 0) {
        printf("Matrix is singular, inverse not possible.\n");
        return;
    }

    double adj[3][3];
    adj[0][0] = (MatA[1][1] * MatA[2][2] - MatA[1][2] * MatA[2][1]);
    adj[0][1] = -(MatA[1][0] * MatA[2][2] - MatA[1][2] * MatA[2][0]);
    adj[0][2] = (MatA[1][0] * MatA[2][1] - MatA[1][1] * MatA[2][0]);
    adj[1][0] = -(MatA[0][1] * MatA[2][2] - MatA[0][2] * MatA[2][1]);
    adj[1][1] = (MatA[0][0] * MatA[2][2] - MatA[0][2] * MatA[2][0]);
    adj[1][2] = -(MatA[0][0] * MatA[2][1] - MatA[0][1] * MatA[2][0]);
    adj[2][0] = (MatA[0][1] * MatA[1][2] - MatA[0][2] * MatA[1][1]);
    adj[2][1] = -(MatA[0][0] * MatA[1][2] - MatA[0][2] * MatA[1][0]);
    adj[2][2] = (MatA[0][0] * MatA[1][1] - MatA[0][1] * MatA[1][0]);

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            MatB[i][j] = adj[i][j] / det;
}

double YourName_Mod(double MatA[][3]) {
    return determinant(MatA);
}

