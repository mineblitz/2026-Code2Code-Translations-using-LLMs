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
int digitSum(string s){
    int sum=0;
    for (int i=0;i<s.length();i++)
        if (s[i]>=65 and s[i]<=90)
            sum+=s[i];
    return sum;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    int result = digitSum(n);
    std::cout << result << std::endl;
}
