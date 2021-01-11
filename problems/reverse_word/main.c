#include <stdio.h>
#include "string.h"

void reverse_word(char input[]){
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
    printf("Give a 'word'");
    scanf("%s", &input);
    reverse_word(input);
    return 0;
}
