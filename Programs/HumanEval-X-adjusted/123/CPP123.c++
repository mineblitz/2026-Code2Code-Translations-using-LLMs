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
vector<int> get_odd_collatz(int n){
    vector<int> out={1};
    while (n!=1)
    {
        if (n%2==1) {out.push_back(n); n=n*3+1;}
        else n=n/2;
    }
    sort(out.begin(),out.end());
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    vector<int> result = get_odd_collatz(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
