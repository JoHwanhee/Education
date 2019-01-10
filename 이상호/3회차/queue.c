#include <stdio.h>
#include <stdlib.h>

typedef struct quque {
	int* array;
	int size, front, rear, capacity;
} Queue;

Queue* createQueue(int capacity);
int isFull(Queue* queue);
int isEmpty(Queue* queue);
void enqueue(Queue* queue, int data);
int dequeue(Queue* queue);
int front(Queue* queue);
int rear(Queue* queue);

int main(void)
{
	Queue* queue = createQueue(10);
	printf("¿ë·® : %d ", queue->capacity);
	enqueue(queue, 6);
	enqueue(queue, 16);
	enqueue(queue, 26);
	enqueue(queue, 36);
	enqueue(queue, 46);
	enqueue(queue, 56);
	enqueue(queue, 66);

	for (int i = 0; i < queue->size; ++i)
	{
		printf("%d ", queue->array[i]);
	}

	

	return 0;
}

Queue * createQueue(int capacity)
{
	Queue* queue = (Queue*)malloc(sizeof(Queue));
	queue->array = (int*)malloc(sizeof(int) * capacity);
	
	if(queue->array == NULL)
	{
		printf("Heap over.");
	}
	
	queue->capacity = capacity;
	queue->front = 0;
	queue->rear = 0;
	queue->size = 0;

	return queue;
}

int isFull(Queue * queue)
{
	return queue->size == queue->capacity;
}

int isEmpty(Queue * queue)
{
	return queue->size == 0;
}

void enqueue(Queue * queue, int data)
{
	if(queue == NULL)
	{
		printf("Queue is null.");
		return;
	}

	if(isFull(queue))
	{
		printf("Queue is full.");
		return;
	}

	if(isEmpty(queue))
	{
		queue->array[queue->rear] = data;
	}
	else
	{
		queue->rear = (queue->rear + 1);
		queue->array[queue->rear] = data;
	}

	queue->size++;

	printf("enqueue : %d \n", queue->array[queue->rear]);
}

int dequeue(Queue * queue)
{
	if (queue == NULL)
	{
		printf("Queue is null.");
		return;
	}

	if (isEmpty(queue))
	{
		printf("Queue is empty.");
		return;
	}

	int retrun_data = queue->array[queue->front];
	queue->front = queue->front + 1;
	queue->size--;
	return retrun_data;
}

int front(Queue * queue)
{
	return queue->array[queue->front];
}

int rear(Queue * queue)
{
	return queue->array[queue->rear];
}
