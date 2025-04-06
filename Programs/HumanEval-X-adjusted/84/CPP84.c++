#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
string solve(int N){
    string str,bi="";
    str=to_string(N);
    int i,sum=0;
    for (int i=0;i<str.length();i++)
        sum+=str[i]-48;
    while (sum>0)
    {
        bi=to_string(sum%2)+bi;
        sum=sum/2;
    }
    return bi;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    string result = solve(n);
    std::cout << result << std::endl;
}
