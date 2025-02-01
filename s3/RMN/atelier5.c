/*Richard ENG, Nawad KHARILLA, Ines HARRAOUI*/

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

uint64_t add(uint32_t a, uint32_t b, uint32_t p){
    uint64_t ad=a+b;
    return ad % p;
}

uint64_t sub(uint32_t a, uint32_t b, uint32_t p){ 
    uint64_t as=a-b;  
    return as % p;
}

uint64_t mul(uint32_t a, uint32_t b){
    uint64_t p=a*b;
    return p;
}

uint64_t mul_mod(uint32_t a, uint32_t b, uint32_t p){
    return mul(a,b) %p;
}

uint32_t inv(uint32_t a, uint32_t p){
    int u1=1, u2=0, u3=a;
    int v1=0, v2=1, v3=p;
    int t1,t2,t3;

    while(v3!=0){
        int q=u3/v3;
        t1= u1-q*v1;
        t2= u2-q*v2;
        t3= u3-q*v3;
        
        u1=v1;
        u2=v2;
        u3=v3;
        v1=t1;
        v2=t2;
        v3=t3;
    }

    if (u1<0){
        u1+=p;
    }
    return u1;
}

void split_64 (uint64_t a, uint32_t *a1, uint32_t *a0){
    *a1 = a / (2<<30); // (a >> 31)
    *a0 = a - (*a1)*(2<<30); // a%(2<<31)
}

void mul_naive_128 (uint64_t a, uint64_t b, uint64_t *ab2, uint64_t *ab1, uint64_t *ab0){
    uint32_t a0,a1,b0,b1;
    split_64(a, &a0,&a1);
    split_64(b, &b0,&b1); 

    *ab2 = mul(a1,b1);
    *ab1 = mul(a1,b0) + mul(a0,b1);
    *ab0 = mul(a0,b0);
}

void mul_karatsuba_128 (uint64_t a, uint64_t b, uint64_t *ab2, uint64_t *ab1, uint64_t *ab0){
    uint32_t a0,a1,b0,b1;
    split_64(a, &a0,&a1);
    split_64(b, &b0,&b1);

    mul_naive_128(a,b,ab2,ab1,ab0);
    *ab2 = mul(a1,b1);
    *ab0 = mul(a0,b0);
    *ab1 = mul((a1 + a0),(b1 + b0)) - mul((*ab2),(*ab0));
}

int main(){
    
    // PARTIE 1

    uint32_t af = 2, bf = 2, p = 1073741827; 

    /*uint32_t add_afbf = add (af,bf,2);
    printf("add_afbf = %d\n", add_afbf);
    uint32_t add_afbf = add (af,bf,101);
    printf("add_afbf = %d\n", add_afbf);
    uint32_t add_afbf = add (af,bf,65521);
    printf("add_afbf = %d\n", add_afbf);*/
    uint32_t add_afbf = add (af,bf,p);
    printf("add_afbf = %d\n", add_afbf);

    /*uint32_t s = sub(af, bf, 2);
    printf("s = %u\n", s);
    uint32_t s = sub(af, bf, 101);
    printf("s = %u\n", s);
    uint32_t s = sub(af, bf, 65521);
    printf("s = %u\n", s);*/
    uint32_t s = sub(af, bf, p);
    printf("s = %u\n", s);

    uint64_t m = mul(af, bf);
    printf("m = %u\n", m);

    /*uint64_t mmod = mul_mod(af, bf, 2);
    printf("mmod = %u\n", mmod);
    uint64_t mmod = mul_mod(af, bf, 101);
    printf("mmod = %u\n", mmod);
    uint64_t mmod = mul_mod(af, bf, 65521);
    printf("mmod = %u\n", mmod);*/
    uint64_t mmod = mul_mod(af, bf, p);
    printf("mmod = %u\n", mmod);

    /*uint32_t i=inv(af,2);
    printf("i = %u\n", i);
    uint32_t i=inv(af,101);
    printf("i = %u\n", i);
    uint32_t i=inv(af,65521);
    printf("i = %u\n", i);*/
    uint32_t i=inv(af,p);
    printf("i = %u\n", i);

    // PARTIE 2

    uint64_t ad = (2<<30)+1; 
    uint32_t a1, a0;
    
    split_64(ad,&a1,&a0);
    printf("a1 : %u ; a0 : %u\n",a1,a0);
    
    uint64_t ap=12482, bp=1740050;
    uint64_t ab0, ab1, ab2;

    mul_naive_128(ap,bp,&ab2,&ab1,&ab2);
    printf("ab2 : %d ; ab1 : %d ; ab0 : %d\n",ab2,ab1,ab0);

    mul_karatsuba_128(ap,bp,&ab2,&ab1,&ab2);
    printf("ab2 : %d ; ab1 : %d ; ab0 : %d\n",ab2,ab1,ab0);
    
    return 0;
}