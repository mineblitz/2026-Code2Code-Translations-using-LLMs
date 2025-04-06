#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
int greatest_common_divisor(int a, int b){
    int out,m;
    while (true){
        if (a<b) 
        {
            m=a;a=b;b=m;
        }
        a=a%b;
        if (a==0) return b;
    }
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    int result = greatest_common_divisor(n, o);
    std::cout << result << std::endl;
}
