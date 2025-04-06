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
vector<int> unique_digits(vector<int> x){
    vector<int> out={};
    for (int i=0;i<x.size();i++)
        {
            int num=x[i];
            bool u=true;
            if (num==0) u=false;
            while (num>0 and u)
            {
                if (num%2==0) u=false;
                num=num/10;
            }
            if (u) out.push_back(x[i]);
        }
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
    vector<int> result = unique_digits(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
