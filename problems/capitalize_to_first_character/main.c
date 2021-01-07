#include <stdio.h>
#define value 'a'-'A'

char capitalizeToFirstChar(char sentence[100]){
    int index = 0;
    while(sentence[index]!='\0'){
        if(index==0){
            if(sentence[index]>='a' && sentence[index]<='z'){
                sentence[index] -= value;
            }
        }if(sentence[index]==' '){
            index++;
            if(sentence[index]>='a' && sentence[index]<='z'){
                sentence[index] -= value;
            }
        }
        index++;
    }
    return &sentence;
}

int main() {
    char sentence[100];
    printf("Give to sentence!\n");
    fgets(&sentence, 100, stdin);
    sentence[100] = capitalizeToFirstChar(sentence);
    printf("%s", sentence);
    return 0;
}
