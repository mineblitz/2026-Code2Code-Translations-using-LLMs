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
vector<string> total_match(vector<string> lst1,vector<string> lst2){
    int num1,num2,i;
    num1=0;num2=0;
    for (i=0;i<lst1.size();i++)
        num1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
        num2+=lst2[i].length();
    if (num1>num2) return lst2;
    return lst1;
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
    vector<string> result = total_match(n, o);
cout << "[";
for (size_t i = 0; i < result.size(); ++i) {
result[i].erase(std::remove(result[i].begin(), result[i].end(), '\''), result[i].end());
    cout << "'" << result[i] << "'";
    if (i != result.size() - 1) {
        std::cout << ", ";
    }
}
cout << "]" << endl;
}
