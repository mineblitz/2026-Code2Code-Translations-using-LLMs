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
int strlen(string str){
    return str.length();
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    int result = strlen(n);
    std::cout << result << std::endl;
}
