#include "../../../module/include/ops.h"

// gives back the nth fibonacci number
int fibonacci(unsigned int n){
    if((n == 0) || (n == 1)){
        return n;
    }
    int fibo_0 = 0;
    int fibo_1 = 1;
    int accum = 0;
    for(unsigned int i = 2; i<=n; i++){
        accum = fibo_0 + fibo_1;
        fibo_0 = fibo_1;
        fibo_1 = accum;
    }
    return accum;
}