int signeProduit(int a, int b) {

if (a*b==0)
{
return 0;
}

if (a*b<0) {
    return -1;
}

return 1;
}
