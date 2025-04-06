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
string exchange(vector<int> lst1,vector<int> lst2){
    int num=0;
    for (int i=0;i<lst1.size();i++)
    if (lst1[i]%2==0) num+=1;
    for (int i=0;i<lst2.size();i++)
    if (lst2[i]%2==0) num+=1;
    if (num>=lst1.size()) return "YES";
    return "NO";
}
    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    int myValue0;
    std::vector<int> n;
    while ( iss0 >> myValue0 )
        n.push_back( myValue0 );
    string input1 = argv[2];
    if (input1.front() == '[') input1.erase(0, 1);
    if (input1.back() == ']') input1.pop_back();
    input1.erase(std::remove(input1.begin(), input1.end(), ','), input1.end());
    std::stringstream iss1( input1 );
    int myValue1;
    std::vector<int> o;
    while ( iss1 >> myValue1 )
        o.push_back( myValue1 );
    string result = exchange(n, o);
    std::cout << result << std::endl;
}
