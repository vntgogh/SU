void f(int a,int b,int c,int *p_a,int *p_b,int *p_c){
  a=b;
  p_a=p_b;
  b=(*p_a)*c;
  p_c=&b;
  *p_b=*p_c+a;
}

int main() {
    int a=5;
    int b=3;
    int c=2;
    f(a,b,c,&a,&b,&c);
    printf("%d, %d, %d\n", a,b,c);
    return 0;
}
