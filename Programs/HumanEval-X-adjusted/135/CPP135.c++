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
int can_arrange(vector<int> arr){
    int max=-1;
    for (int i=0;i<arr.size();i++)
    if (arr[i]<=i) max=i;
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
    int result = can_arrange(n);
    std::cout << result << std::endl;
}
