#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int data;
	struct node* link;
} Node;

Node *top;

void push(int data)
{
	Node *newNode = malloc(sizeof(Node));
	newNode->data = data;
	newNode->link = top;

	top = newNode;
}

int pop()
{
	Node *temp = top->link;
	free(top);
	top = temp;

	return top->data;
}

int pick()
{
	if(top == NULL)
	{
		printf("top is null");
		exit(1);
	}

	return top->data;
}

void printStack()
{
	Node* temp = top;
	int i;
	for(i = 0; temp != NULL; i++)
	{
		printf("%d->", temp->data);
		temp = temp->link;
	}
}

int main(void)
{
	push(5);
	push(15);
	push(25);
	push(35);
	printStack();
	push(45);
	push(55);
	printf("\n\n\n");
	printStack();

	printf("PICK : %d", pick());

	return 0;
}

