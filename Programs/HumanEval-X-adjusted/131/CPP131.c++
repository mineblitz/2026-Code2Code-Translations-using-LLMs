#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
#include<stdlib.h>
int digits(int n){
    int prod=1,has=0;
    string s=to_string(n);
    for (int i=0;i<s.length();i++)
        if (s[i]%2==1) 
        {
            has=1;
            prod=prod*(s[i]-48);
        }
    if (has==0) return 0;
    return prod;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = digits(n);
    std::cout << result << std::endl;
}
