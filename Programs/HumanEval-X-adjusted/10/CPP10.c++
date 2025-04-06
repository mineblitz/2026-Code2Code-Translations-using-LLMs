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
bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}
string make_palindrome(string str){
   int i;
   for (i=0;i<str.length();i++)
   {
        string rstr=str.substr(i);
        if (is_palindrome(rstr))
        {
            string nstr;
            nstr=str.substr(0,i);
            string n2str(nstr.rbegin(),nstr.rend());
            return str+n2str;
        }
   }
   string n2str(str.rbegin(),str.rend());
   return str+n2str;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = make_palindrome(n);
    std::cout << result << std::endl;
}
