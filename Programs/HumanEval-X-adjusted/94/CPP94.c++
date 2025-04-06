#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int skjkasdkd(vector<int> lst){
    int largest=0;
    for (int i=0;i<lst.size();i++)
        if (lst[i]>largest)
        {
            bool prime=true;
            for (int j=2;j*j<=lst[i];j++)
                if (lst[i]%j==0) prime=false;
            if (prime) largest=lst[i];
        }
    int sum=0;
    string s;
    s=to_string(largest);
    for (int i=0;i<s.length();i++)
        sum+=s[i]-48;
    return sum;
}
#undef NDEBUG
#include<assert.h>
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
    int result = skjkasdkd(n);
    std::cout << result << std::endl;
}
