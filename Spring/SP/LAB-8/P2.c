#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]){
	int opt;
	while((opt=getopt(argc, argv,":if:lr")) !=-1){
		switch(opt){
			case 'i':
			case 'l':
			case 'r':
				printf("option: %c\n", opt);
				break;
			case 'f':
				printf("filename: %s\n", optarg);
				break;
			case ':':
				printf("opt need value \n");
				break;
			case '?':
				printf("unknown opt %c\n", optopt);
				break;
		}
	}	
	for (; optind <argc; optind++){
		printf("arg: %s\n:", argv[optind]);

	}
	exit(0);
}

