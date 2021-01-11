#include <stdio.h>

void swap(int * val1, int * val2){
    int temp;
    temp = *val1;
    *val1 = *val2;
    *val2 = temp;
}

int main() {
    int val1, val2;
    printf("enter two number!\n");
    scanf("%d %d", &val1, &val2);
    printf("before swap: val1:%d val2:%d \n", val1, val2);
    swap(&val1, &val2);
    printf("after swap: val1:%d val2:%d \n", val1, val2);
    return 0;
}
