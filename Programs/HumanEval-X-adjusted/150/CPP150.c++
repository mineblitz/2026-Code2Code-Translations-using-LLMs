#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
#include<stdlib.h>
int x_or_y(int n,int x,int y){
    bool isp=true;
    if (n<2) isp=false;
    for (int i=2;i*i<=n;i++)
    if (n%i==0) isp=false;
    if (isp) return x;
    return y;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    int p = atoi(argv[3]);
    int result = x_or_y(n, o, p);
    std::cout << result << std::endl;
}
