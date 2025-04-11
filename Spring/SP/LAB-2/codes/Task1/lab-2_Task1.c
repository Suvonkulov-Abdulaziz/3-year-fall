#include <stdio.h>
#include <stdlib.h>

int main(){
	int id=001;
	char  name[]="Abdulaziz";
	float mark[5]={1,2,3,5,6};
	printf("%s\n", name );
	printf("%d\n", id);
 	for(int i=0;i<5;i++){
		printf("Grade: %f\n", mark[i]);
	}
}

