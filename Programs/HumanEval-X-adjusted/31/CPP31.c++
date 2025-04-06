#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
bool is_prime(long long n){
    if (n<2) return false;
    for (long long i=2;i*i<=n;i++)
        if (n%i==0) return false;
    return true;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    bool result = is_prime(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
