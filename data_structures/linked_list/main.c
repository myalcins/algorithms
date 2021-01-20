#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int value;
    struct Node * next;
}Node;

Node * create_head(){
    Node * head = (Node *)malloc(sizeof (Node));
    head->next = NULL;
    return head;
}

Node * create_node(int value){
    Node * new = (Node *)malloc(sizeof (Node));
    new->value = value;
    new->next = NULL;
    return new;
}

void add_node(int value, Node * head){
    while(head->next != NULL){
        head = head->next;
    }
    Node * new = create_node(value);
    head->next = new;
}

void print_linked_list(Node * head){
    while (head->next != NULL){
        head = head->next;
        printf("%d \n", head->value);
    }
}

int main() {
    Node * head = create_head();
    add_node(5,head);
    add_node(7,head);
    print_linked_list(head);
    return 0;
}
