#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<string>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
string string_xor(string a,string b){
    string output="";
    for (int i=0;(i<a.length() and i<b.length());i++)
    {
        if (i<a.length() and i<b.length())
        {
            if (a[i]== b[i]) 
            {
                output+='0';
            }  
            else output+='1';
        }
        else
        {
            if (i>=a.length()) 
            {
            output+=b[i];
            }
            else output+=a[i];
        }
    }
    return output;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string o = argv[2];
    string result = string_xor(n, o);
    std::cout << result << std::endl;
}
