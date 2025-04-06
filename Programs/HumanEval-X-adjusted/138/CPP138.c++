#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
#include<stdlib.h>
bool is_equal_to_sum_even(int n){
    if (n%2==0 and n>=8) return true;
    return false;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    bool result = is_equal_to_sum_even(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
