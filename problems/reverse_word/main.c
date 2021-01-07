#include <stdio.h>
#include "string.h"

void reverseWord(char input[]){
    int begin = strlen(input);
    char output[begin];
    int index = 0;
    while(begin>=0){
        output[index] = input[begin-1];
        begin--;
        index++;
    }
    printf("%s", &output);
}

int main(){
    char input[100];
    printf("Give to words");
    scanf("%s", &input);
    reverseWord(input);
    return 0;
}
