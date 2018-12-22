#include <stdio.h>
#include <stdlib.h>


typedef struct node
{
	int data;
	struct node* next;

} Node;
 

Node* head;

// add
void add(int data, int index)
{
	if (index == 1)
	{
		Node* newNode = (Node *)malloc(sizeof(Node));
		newNode->data = data;
		newNode->next = NULL;

		head->next = newNode;

		return;
	}

	Node* temp = head;
	for (int i = 0; i < index - 1; i++)
	{
		temp = temp->next;
	}

	Node* newNode = (Node *)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = temp->next;

	temp->next = newNode;
}

void printList()
{
	Node* temp = head;
	for (int i = 0; temp != NULL; i++)
	{
		printf("[%d] %d \n", i, temp->data);
		temp = temp->next;
	}
}

// remove

int main()
{
	head = (Node *)malloc(sizeof(Node));

	head->data = 5;
	add(10, 1);
	add(15, 2);
	add(20, 3);
	add(25, 4);

	add(10000, 2);

	printList();
}