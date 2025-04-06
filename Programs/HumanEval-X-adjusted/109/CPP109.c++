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
bool move_one_ball(vector<int> arr){
    int num=0;
    if (arr.size()==0) return true;
    for (int i=1;i<arr.size();i++)
        if (arr[i]<arr[i-1]) num+=1;
    if (arr[arr.size()-1]>arr[0]) num+=1;
    if (num<2) return true;
    return false;
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
    bool result = move_one_ball(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
