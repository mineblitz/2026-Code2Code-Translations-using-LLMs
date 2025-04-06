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
vector<int> make_a_pile(int n){
    vector<int> out={n};
    for (int i=1;i<n;i++)
        out.push_back(out[out.size()-1]+2);
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    vector<int> result = make_a_pile(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
