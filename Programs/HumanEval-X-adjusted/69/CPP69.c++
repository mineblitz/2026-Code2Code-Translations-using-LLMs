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
int search(vector<int> lst){
    vector<vector<int>> freq={};
    int max=-1;
    for (int i=0;i<lst.size();i++)
    {
        bool has=false;
        for (int j=0;j<freq.size();j++)
            if (lst[i]==freq[j][0]) 
            {
            freq[j][1]+=1;
            has=true;
            if (freq[j][1]>=freq[j][0] and freq[j][0]>max) max=freq[j][0];
            }
        if (not(has)) 
        {
        freq.push_back({lst[i],1});
        if (max==-1 and lst[i]==1) max=1;
        }
    }
    return max;
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
    int result = search(n);
    std::cout << result << std::endl;
}
