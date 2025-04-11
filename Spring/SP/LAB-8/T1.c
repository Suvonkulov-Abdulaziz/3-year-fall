#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>
#define _GNU_SOURCE

int main(int argc, char *argv[]){
	if (argc != 2){
		printf("usage is %s [options]", argv[0]);
		exit(EXIT_FAILURE);
	}
	int opt;
	struct option longopts[]={
		{"help", 0 ,NULL, 'h'},
		{"version", 0, NULL, 'v'},
		{"info", 0, NULL, 'i'},
		{0,0,0,0},
	};
	while((opt= getopt_long(argc,argv,"hvi",longopts,NULL))!=1){
		switch(opt){	
			case 'h':
				printf("help");
				break;
			case 'v':
			case 'i':
			case '?':
			default:
				printf("usage is %s [opitons] --help \n", argv[0]);
		}
	}	
	exit(EXIT_SUCCESS);
}
