#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int bucket[MAX];

void add(int data, int index);
void remove(int index);
void printItem();
void length();

int main() {

	add(10, 0);
	printItem();

	return 0;
}

void add(int data, int index)
{
	int i = 0;
	int j = index;
	int tempArray[MAX];

	for (i = 0; i < MAX; i++, j++) {
		tempArray[i] = bucket[j];
	}

	for (i = index; i < MAX; i++) {
		bucket[i] = 0;
	}

	bucket[index] = data;

	j = index + 1;
	for (i = 0; i < MAX; i++, j++) {
		tempArray[i] = bucket[j];
	}
}

void remove(int index)
{
}

void printItem()
{
	int i = 0;
	for (; i < MAX; i++) {
		printf("%d \n", *(bucket + i));
	}
}

void length()
{
}
