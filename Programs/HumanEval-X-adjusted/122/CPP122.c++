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
int add_elements(vector<int> arr,int k){
    int sum=0;
    for (int i=0;i<k;i++)
        if( arr[i]>=-99 and arr[i]<=99)
            sum+=arr[i];
    return sum;
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
    int o = atoi(argv[2]);
    int result = add_elements(n, o);
    std::cout << result << std::endl;
}
