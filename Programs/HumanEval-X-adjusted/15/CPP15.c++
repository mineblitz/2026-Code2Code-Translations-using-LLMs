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
string string_sequence(int n){
    string out="0";
    for (int i=1;i<=n;i++)
    out=out+" "+to_string(i);
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    string result = string_sequence(n);
    std::cout << result << std::endl;
}
