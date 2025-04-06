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
string decimal_to_binary(int decimal){
    string out="";
    if (decimal==0) return "db0db";
    while (decimal>0)
    {
        out=to_string(decimal%2)+out;
        decimal=decimal/2;
    }
    out="db"+out+"db";
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    string result = decimal_to_binary(n);
    std::cout << result << std::endl;
}
