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
int closest_integer(string value){
    double w;
    w=atof(value.c_str());
    return round(w);
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    int result = closest_integer(n);
    std::cout << result << std::endl;
}
