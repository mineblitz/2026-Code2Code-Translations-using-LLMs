#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
#include<stdlib.h>
long long special_factorial(int n){
    long long fact=1,bfact=1;
    for (int i=1;i<=n;i++)
    {
        fact=fact*i;
        bfact=bfact*fact;
    }
    return bfact;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    long long result = special_factorial(n);
    std::cout << result << std::endl;
}
