#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
#include<stdlib.h>
vector<string> by_length(vector<int> arr){
    map<int,string> numto={{0,"Zero"},{1,"One"},{2,"Two"},{3,"Three"},{4,"Four"},{5,"Five"},{6,"Six"},{7,"Seven"},{8,"Eight"},{9,"Nine"}};
    sort(arr.begin(),arr.end());
    vector<string> out={};
    for (int i=arr.size()-1;i>=0;i-=1)
        if (arr[i]>=1 and arr[i]<=9)
        out.push_back(numto[arr[i]]);
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
    vector<string> result = by_length(n);
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
