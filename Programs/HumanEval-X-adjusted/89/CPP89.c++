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
string encrypt(string s){
    string out;
    int i;
    for (i=0;i<s.length();i++)
    {
        int w=((int)s[i]+4-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = encrypt(n);
    std::cout << result << std::endl;
}
