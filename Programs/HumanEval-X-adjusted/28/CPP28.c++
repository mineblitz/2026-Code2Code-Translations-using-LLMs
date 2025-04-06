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
string concatenate(vector<string> strings){
    string out="";
    for (int i=0;i<strings.size();i++)
        out=out+strings[i];
    return out;
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
    string result = concatenate(n);
    std::cout << result << std::endl;
}
