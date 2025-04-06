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
vector<int> count_up_to(int n){
    vector<int> out={};
    int i,j;
    for (i=2;i<n;i++)
        if (out.size()==0) {out.push_back(i);}
        else
        {
            bool isp=true;
            for (j=0;out[j]*out[j]<=i;j++)
                if (i%out[j]==0) isp=false;
            if (isp) out.push_back(i);
        }
    return out;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    vector<int> result = count_up_to(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
