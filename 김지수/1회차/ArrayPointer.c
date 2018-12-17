#include <stdio.h>
#include <stdlib.h>

int pointerarray();
void printArray(int *arr, int size);

struct Week {
	int Monday;
	int Tuesday;
} typedef Week;

typedef int* IntP;

int main(){
	int arr[4];
	arr[0] = 10;
	arr[1] = 10;
	arr[2] = 10;
	arr[3] = 10;
	
	pointerarray();
	printArray(arr, 4);
}

int pointerarray()
{
	int i = 0;
	int *p = (int *)malloc(sizeof(int) * 4);
	
	for (i; i < 4; i++) {
		printf("%d", *(p + i));
	}
}

void printArray(int * arr, int size)
{
	int i = 0;
	for (; i < size; i++) {
		printf("%d \n", *(arr + i));
	}
}
