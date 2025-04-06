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
vector<int> sort_array(vector<int> arr){
    vector<int> bin={};
    int m;

    for (int i=0;i<arr.size();i++)
    {
        int b=0,n=abs(arr[i]);
        while (n>0)
        {
            b+=n%2;n=n/2;
        }
        bin.push_back(b);
    }
    for (int i=0;i<arr.size();i++)
    for (int j=1;j<arr.size();j++)
    if (bin[j]<bin[j-1] or (bin[j]==bin[j-1] and arr[j]<arr[j-1]))
    {
        m=arr[j];arr[j]=arr[j-1];arr[j-1]=m;
        m=bin[j];bin[j]=bin[j-1];bin[j-1]=m;
    }
    return arr;
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
    vector<int> result = sort_array(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
