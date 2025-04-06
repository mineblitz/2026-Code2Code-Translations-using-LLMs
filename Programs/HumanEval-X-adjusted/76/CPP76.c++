#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
bool is_simple_power(int x,int n){
    int p=1,count=0;
    while (p<=x and count<100)
    {
        if (p==x) return true;
        p=p*n;count+=1;
    }
    return false;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    bool result = is_simple_power(n, o);
    std::cout << (result ? "True" : "False") << std::endl;
}
