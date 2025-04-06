#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
#include<algorithm>
#include<stdlib.h>
vector<float> rescale_to_unit(vector<float> numbers){ 
    float min=100000,max=-100000;
    for (int i=0;i<numbers.size();i++)
        {
            if (numbers[i]<min) min=numbers[i];
            if (numbers[i]>max) max=numbers[i];
        }
    for (int i=0;i<numbers.size();i++)
        numbers[i]=(numbers[i]-min)/(max-min);
    return numbers;
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
    vector<float> result = rescale_to_unit(n);
cout << "[";
for (size_t i = 0; i < result.size(); ++i) {
    cout << result[i];
    if (i != result.size() - 1) {
        std::cout << ", ";
    }
}
cout << "]" << endl;
}
