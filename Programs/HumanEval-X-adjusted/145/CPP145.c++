#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#include<stdlib.h>
vector<int> order_by_points(vector<int> nums){
    vector<int> sumdigit={};
    for (int i=0;i<nums.size();i++)
    {
        string w=to_string(abs(nums[i]));
        int sum=0;
        for (int j=1;j<w.length();j++)
            sum+=w[j]-48;
        if (nums[i]>0) sum+=w[0]-48;
        else sum-=w[0]-48;
        sumdigit.push_back(sum);
    }
    int m;
    for (int i=0;i<nums.size();i++)
    for (int j=1;j<nums.size();j++)
    if (sumdigit[j-1]>sumdigit[j])
    {
        m=sumdigit[j];sumdigit[j]=sumdigit[j-1];sumdigit[j-1]=m;
        m=nums[j];nums[j]=nums[j-1];nums[j-1]=m;
    }
     
    return nums;
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
    vector<int> result = order_by_points(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
