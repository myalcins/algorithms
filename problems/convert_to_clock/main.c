#include <stdio.h>
void convertToClock(int value){
    int hour, min;
    hour = value/60;
    min = value-(60*hour);
    printf("h:m %d:%d \n", hour, min);

}

int main() {
    int value;
    printf("Give a value!\n");
    scanf("%d", &value);
    convertToClock(value);
    return 0;
}
