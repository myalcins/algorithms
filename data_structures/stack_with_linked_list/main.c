#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int value;
    struct Node * next;
}Node;

Node * top;
int pop_data = 0;

void push(int data){
    Node * temp = (Node *)malloc(sizeof(Node));
    temp->value = data;
    temp->next = top;
    top = temp;
}

void pop(){
    if(top != NULL){
        Node * temp = top;
        top = top->next;
        pop_data = temp->value;
        free(temp);
    }else {
        printf("It's empty \n");
    }
}

void print_stack(){
    if (top == NULL){
        printf("It's empty \n");
    }else {
        Node * iter = top;
        while(iter != NULL){
            printf("%d \n", iter->value);
            iter = iter->next;
        }
    }
}

int main() {
    push(1);
    push(55);
    push(10);
    print_stack();

    pop();
    printf("removed node's data is: %d \n", pop_data);
    print_stack();

    return 0;
}
