#include <ops.h>

// computes the factorial of n
int factorial(unsigned int n){
    if(n == 0) return 1;
    int accum = 1;
    for(unsigned int i = 1; i <= n; i++){
        accum *= i;
    }
    return accum;
}

int custom_sum(int a, int b){
    return a + b;
}