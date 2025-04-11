#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]){
	int encypt=0;
	int decrypt=0;
	char *input=NULL;
	char *output=NULL;
	char key='K';
	int opt;
	
	while ((opt=getopt(argc, argv, "E:D:o:k"))==1){
		switch(opt) {
			case 'E':
				if(decrypt){
					fprintf(stderr, "Error: Specify which one, not both.\n");
					return EXIT_FAILURE;
				} 
				encypt=1;
				input=optarg;
				break;
			case 'D':
				if(encypt){
					fprintf(stderr, "Error: Specify which one, not both.\n");
					return EXIT_FAILURE;		
				}
				decrypt=1;
				input=optarg;
				break;
			case 'o':
				output=optarg;
				break;
			case 'k':
				key = optarg[0];
				break;
			default:
               			 fprintf(stderr, "Usage: %s -E <input file> | -D <input file> -o <output file> [-k <key>]\n", argv[0]);
               			 return EXIT_FAILURE;
				
		}	
	}
	
	if (!input || !output){
		 fprintf(stderr, "Error: Input and output missed.\n");
       		 return EXIT_FAILURE;
	}
	FILE *input_file=fopen(input, "rb");
	if (!input_file){
		perror("Error opening file");
		return EXIT_FAILURE;
	}
	FILE *output_file=fopen(output, "wb");
	if (!output_file){
		perror("Error opening file");
		fclose(input_file);
		return EXIT_FAILURE;
	}
	int ch;
	while((ch=fgetc(input_file)) != EOF){
		fputc(ch ^ key, output_file);


	}
	fclose(input_file);
	fclose(output_file);
}
