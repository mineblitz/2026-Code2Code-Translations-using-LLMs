#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
float truncate_number(float number){
    return number-int(number);
}
    int main(int argc, char *argv[]) {
    float n = atof(argv[1]);
    float result = truncate_number(n);
    std::cout << result << std::endl;
}
