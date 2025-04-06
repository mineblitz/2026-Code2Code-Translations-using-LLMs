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
int count_upper(string s){
    string uvowel="AEIOU";
    int count=0;
    for (int i=0;i*2<s.length();i++)
    if (find(uvowel.begin(),uvowel.end(),s[i*2])!=uvowel.end())
        count+=1;
    return count;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    int result = count_upper(n);
    std::cout << result << std::endl;
}
