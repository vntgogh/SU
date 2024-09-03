#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int n=967;

    while(n>0){
        int res=n%(-2);
        n/=(-2); 
        if(res<0){
            res+=2;
            printf("%d", res);
        }else{
            printf("%d", res);
        }
    }
}