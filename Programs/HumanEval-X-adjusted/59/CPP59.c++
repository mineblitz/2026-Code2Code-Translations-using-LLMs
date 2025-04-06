#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int largest_prime_factor(int n){
    for (int i=2;i*i<=n;i++)
    while (n%i==0 and n>i)  n=n/i;
    return n;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = largest_prime_factor(n);
    std::cout << result << std::endl;
}
