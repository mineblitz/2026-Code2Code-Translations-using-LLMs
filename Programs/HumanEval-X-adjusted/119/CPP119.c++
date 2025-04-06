#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
string match_parens(vector<string> lst){
    string l1=lst[0]+lst[1];
    int i,count=0;
    bool can=true;
    for (i=0;i<l1.length();i++)
        {
            if (l1[i]=='(') count+=1;
            if (l1[i]==')') count-=1;
            if (count<0) can=false;
        }
    if (count!=0) return "No";
    if (can==true) return "Yes";
    l1=lst[1]+lst[0];
    can=true;
    for (i=0;i<l1.length();i++)
        {
            if (l1[i]=='(') count+=1;
            if (l1[i]==')') count-=1;
            if (count<0) can=false;
        }
    if (can==true) return "Yes";
    return "No";
}
    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    string myValue0;
    std::vector<string> n;
    while ( iss0 >> myValue0 ){
         myValue0.erase(std::remove(myValue0.begin(), myValue0.end(), '\''), myValue0.end());   
        n.push_back( myValue0 ); }
    string result = match_parens(n);
    std::cout << result << std::endl;
}
