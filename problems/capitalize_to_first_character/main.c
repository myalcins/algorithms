#include <stdio.h>
#define VALUE 'a'-'A'

char capitalize_to_first_char(char sentence[100]){
    int index = 0;
    while(sentence[index]!='\0'){
        if(index==0){
            if(sentence[index]>='a' && sentence[index]<='z'){
                sentence[index] -= VALUE;
            }
        }if(sentence[index]==' '){
            index++;
            if(sentence[index]>='a' && sentence[index]<='z'){
                sentence[index] -= VALUE;
            }
        }
        index++;
    }
    return &sentence;
}

int main() {
    char sentence[100];
    printf("Give a sentence!\n");
    fgets(&sentence, 100, stdin);
    sentence[100] = capitalize_to_first_char(sentence);
    printf("%s", sentence);
    return 0;
}
