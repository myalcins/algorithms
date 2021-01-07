#include <stdio.h>

int factorial(int value){
    if(value == 1)
        return value;
    return value * factorial(value-1);
}

int main() {
    int value;
    printf("Give a number! \n");
    scanf("%d", &value);
    value = factorial( value);
    printf("value! = %d", value);
    return 0;
}
