#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<vector>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
bool below_zero(vector<int> operations){
    int num=0;
    for (int i=0;i<operations.size();i++)
    {
        num+=operations[i];
        if (num<0) return true;
    }
    return false;
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
    bool result = below_zero(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
