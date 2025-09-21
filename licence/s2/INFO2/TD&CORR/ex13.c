#include <stdio.h>
void ma_fonction(int *param1, int param2) {
    int var_loc = 3;
    *param1 = var_loc * param2;
    param2 = var_loc + 1;
}
int main() {
    int v1, v2;
    v1 = 10;
    v2 = 3;
    ma_fonction(&v2,v1);
    printf("%d, %d",v2,v1);
    return 0;
}
