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
vector<int> tri(int n){
    vector<int> out={1,3};
    if (n==0) return {1};
    for (int i=2;i<=n;i++)
    {
        if (i%2==0) out.push_back(1+i/2);
        else out.push_back(out[i-1]+out[i-2]+1+(i+1)/2);
    }
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    vector<int> result = tri(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
