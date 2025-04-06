#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<vector>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
vector<int> generate_integers(int a,int b){
    int m;
    if (b<a)
    {
        m=a;a=b;b=m;
    }

    vector<int> out={};
    for (int i=a;i<=b;i++)
    if (i<10 and i%2==0) out.push_back(i);
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int o = atoi(argv[2]);
    vector<int> result = generate_integers(n, o);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
