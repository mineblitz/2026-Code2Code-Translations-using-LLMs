#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int fib(int n){
    int f[1000];
    f[0]=0;f[1]=1;
    for (int i=2;i<=n; i++)
    f[i]=f[i-1]+f[i-2];
    return f[n];
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = fib(n);
    std::cout << result << std::endl;
}
