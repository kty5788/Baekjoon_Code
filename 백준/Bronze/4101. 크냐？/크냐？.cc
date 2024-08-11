#include <stdio.h>

int main() {
    int num1, num2;
    while(1) {
        scanf("%d %d", &num1, &num2);
        if (num1 == 0 && num2 == 0) {
            return 0;
        }
        if (num1 > num2) {
            printf("Yes\n");
        }
        else {
            printf("No\n");
        }
        
    }
}