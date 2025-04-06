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
string encode(string message){
    string vowels="aeiouAEIOU";
    string out="";
    for (int i=0;i<message.length();i++)
    {
        char w=message[i];
        if (w>=97 and w<=122){w=w-32;}
        else if (w>=65 and w<=90) w=w+32;
        if (find(vowels.begin(),vowels.end(),w)!=vowels.end()) w=w+2;
        out=out+w;
    }
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = encode(n);
    std::cout << result << std::endl;
}
