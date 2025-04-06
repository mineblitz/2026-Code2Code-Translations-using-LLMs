#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int starts_one_ends(int n){
    if (n<1) return 0;
    if (n==1) return 1;
    int out=18;
    for (int i=2;i<n;i++)
        out=out*10;
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = starts_one_ends(n);
    std::cout << result << std::endl;
}
