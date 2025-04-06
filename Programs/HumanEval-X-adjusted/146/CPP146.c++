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
int specialFilter(vector<int> nums){
    int num=0;
    for (int i=0;i<nums.size();i++)
    if (nums[i]>10)
    {
        string w=to_string(nums[i]);
        if (w[0]%2==1 and w[w.length()-1]%2==1) num+=1;
    }
    return num;
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
    int result = specialFilter(n);
    std::cout << result << std::endl;
}
