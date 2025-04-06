#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int sum_to_n(int n){
    return n*(n+1)/2;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = sum_to_n(n);
    std::cout << result << std::endl;
}
