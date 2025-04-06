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
vector<int> common(vector<int> l1,vector<int> l2){
    vector<int> out={};
    for (int i=0;i<l1.size();i++)
        if (find(out.begin(),out.end(),l1[i])==out.end())
            if (find(l2.begin(),l2.end(),l1[i])!=l2.end())
                out.push_back(l1[i]);
    sort(out.begin(),out.end());
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
    string input1 = argv[2];
    if (input1.front() == '[') input1.erase(0, 1);
    if (input1.back() == ']') input1.pop_back();
    input1.erase(std::remove(input1.begin(), input1.end(), ','), input1.end());
    std::stringstream iss1( input1 );
    int myValue1;
    std::vector<int> o;
    while ( iss1 >> myValue1 )
        o.push_back( myValue1 );
    vector<int> result = common(n, o);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
