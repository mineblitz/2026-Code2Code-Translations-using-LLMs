#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#include<stdlib.h>
string Strongest_Extension(string class_name,vector<string> extensions){
    string strongest="";
    int max=-1000;
    for (int i=0;i<extensions.size();i++)
    {
        int strength=0;
        for (int j=0;j<extensions[i].length();j++)
        {
            char chr=extensions[i][j];
            if (chr>=65 and chr<=90) strength+=1;
            if (chr>=97 and chr<=122) strength-=1;
        }
        if (strength>max) 
        {
            max=strength;
            strongest=extensions[i];
        }
    }
    return class_name+'.'+strongest;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string input1 = argv[2];
    if (input1.front() == '[') input1.erase(0, 1);
    if (input1.back() == ']') input1.pop_back();
    input1.erase(std::remove(input1.begin(), input1.end(), ','), input1.end());
    std::stringstream iss1( input1 );
    string myValue1;
    std::vector<string> o;
    while ( iss1 >> myValue1 ){
         myValue1.erase(std::remove(myValue1.begin(), myValue1.end(), '\''), myValue1.end());   
        o.push_back( myValue1 ); }
    string result = Strongest_Extension(n, o);
    std::cout << result << std::endl;
}
