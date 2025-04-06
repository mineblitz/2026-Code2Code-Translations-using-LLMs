#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int modp(int n,int p){
    int out=1;
    for (int i=0;i<n;i++)
        out=(out*2)%p;
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    int result = modp(n, o);
    std::cout << result << std::endl;
}
