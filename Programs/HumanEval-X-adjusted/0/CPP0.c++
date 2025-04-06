#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    float myValue0;
    std::vector<float> n;
    while ( iss0 >> myValue0 )
        n.push_back( myValue0 );
    float o = atof(argv[2]);
    bool result = has_close_elements(n, o);
    std::cout << (result ? "True" : "False") << std::endl;
}
