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
bool is_sorted(vector<int> lst){
    for (int i=1;i<lst.size();i++)
    {
        if (lst[i]<lst[i-1]) return false;
        if (i>=2 and lst[i]==lst[i-1] and lst[i]==lst[i-2]) return false;
    }
    return true;
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
    bool result = is_sorted(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
