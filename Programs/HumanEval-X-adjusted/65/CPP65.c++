#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
string circular_shift(int x,int shift){
    string xs;
    xs=to_string(x);
    if (xs.length()<shift)
    {
        string s(xs.rbegin(),xs.rend());
        return s;
    }
    xs=xs.substr(xs.length()-shift)+xs.substr(0,xs.length()-shift);
    return xs;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    string result = circular_shift(n, o);
    std::cout << result << std::endl;
}
