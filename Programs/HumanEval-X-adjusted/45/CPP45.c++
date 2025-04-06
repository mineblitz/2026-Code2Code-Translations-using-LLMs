#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
float triangle_area(float a,float h){
return (a*h)*0.5;

}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    float result = triangle_area(n, o);
    std::cout << result << std::endl;
}
