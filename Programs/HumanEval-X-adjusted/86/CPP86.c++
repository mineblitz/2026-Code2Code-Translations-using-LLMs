#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
#include<stdlib.h>
string anti_shuffle(string s){
    string out="";
    string current="";
    s=s+' ';
    for (int i=0;i<s.length();i++)
    if (s[i]==' ')
    {
        sort(current.begin(),current.end());
        if (out.length()>0) out=out+' ';
        out=out+current;
        current="";
    }
    else current=current+s[i];
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = anti_shuffle(n);
    std::cout << result << std::endl;
}
