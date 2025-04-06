#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int car_race_collision(int n){
    return n*n;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = car_race_collision(n);
    std::cout << result << std::endl;
}
