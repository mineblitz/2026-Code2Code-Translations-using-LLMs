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
vector<int> maximum(vector<int> arr,int k){
    sort(arr.begin(),arr.end());
    vector<int> out(arr.end()-k,arr.end());
    return out;
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
    int o = atoi(argv[2]);
    vector<int> result = maximum(n, o);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
