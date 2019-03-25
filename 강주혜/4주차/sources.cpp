#include <stdio.h>
#include <stdlib.h>

void countWord(const char* str){
    int charMap[256] = { 0, };
    
    for(int i = 0; str[i] != '\0'; i++) {
        int ch = str[i];
        charMap[ch]++;
    }

    for(int i = 0; i < 256; i++) {
        if( charMap[i] > 0 ){
            printf("%c : %d \n", i, charMap[i]);
        }
    }
}

int getLength(const char* str) {
    const char* tmp = str;
    int count = 0;

    while(*(tmp++))
        count++;

    return count;
}

void itob(int number) {
    int n = number;
    int bitCount = sizeof(int) * 8;
    int* arr = malloc(sizeof(int) * bitCount);

    for( int i = 0; i < bitCount; i ++) {
        arr[i] = (n >> i) & 0x01;
    }

    for(int i = bitCount - 1; i >= 0; i--){
        printf("%d", arr[i]);
        if ( i % 4 == 0){
            printf(" ");
        }
    }
}

void bubbleSort() {
    int arr[10] = {7,6,10,8,9,1,4,5,2,3};
    int bucket = 0;
    for (int i = 0; i < 10; i++){
        for (int j = i; j < 10; j++){
            if ( arr[i] < arr[j] ) {
                bucket = arr[i];
                arr[i] = arr[j];
                arr[j] = bucket;
            }
        }
    }

    for (int i = 0; i < 10; i++){
        printf("%d ", arr[i]);
    }
}

int main (int argc, char* argv[] ) {
    // bubbleSort();
    // itob(5);
    // printf("%d", getLength("Korean"));
    // countWord("klasdjfk ss sskhjf !! s");
    return 0;
}