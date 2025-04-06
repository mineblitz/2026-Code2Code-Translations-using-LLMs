#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
bool right_angle_triangle(float a,float b,float c){
    if (abs(a*a+b*b-c*c)<1e-4 or abs(a*a+c*c-b*b)<1e-4 or abs(b*b+c*c-a*a)<1e-4) return true;
    return false;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    int p = atoi(argv[3]);
    bool result = right_angle_triangle(n, o, p);
    std::cout << (result ? "True" : "False") << std::endl;
}
