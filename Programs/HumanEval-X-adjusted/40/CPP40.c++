#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
#include<stdlib.h>
bool triples_sum_to_zero(vector<int> l){
    for (int i=0;i<l.size();i++)
    for (int j=i+1;j<l.size();j++)
    for (int k=j+1;k<l.size();k++)
        if (l[i]+l[j]+l[k]==0) return true;
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
    bool result = triples_sum_to_zero(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
