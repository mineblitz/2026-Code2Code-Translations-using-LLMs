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
vector<float> find_closest_elements(vector<float> numbers){
    vector<float> out={};
    for (int i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
        if (out.size()==0 or abs(numbers[i]-numbers[j])<abs(out[0]-out[1]))
            out={numbers[i],numbers[j]};
    if (out[0]>out[1])
        out={out[1],out[0]};
    return out;
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
    vector<float> result = find_closest_elements(n);
cout << "[";
for (size_t i = 0; i < result.size(); ++i) {
    cout << result[i];
    if (i != result.size() - 1) {
        std::cout << ", ";
    }
}
cout << "]" << endl;
}
