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
string intersection( vector<int> interval1,vector<int> interval2){
    int inter1,inter2,l,i;
    inter1=max(interval1[0],interval2[0]);
    inter2=min(interval1[1],interval2[1]);
    l=inter2-inter1;
    if (l<2) return "NO";
    for (i=2;i*i<=l;i++)
        if (l%i==0) return "NO";
    return "YES";
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
    string result = intersection(n, o);
    std::cout << result << std::endl;
}
