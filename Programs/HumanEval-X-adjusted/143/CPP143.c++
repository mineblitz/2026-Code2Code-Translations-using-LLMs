#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<string>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
string words_in_sentence(string sentence){
    string out="";
    string current="";
    sentence=sentence+' ';

    for (int i=0;i<sentence.size();i++)
    if (sentence[i]!=' ') current=current+sentence[i];
    else
    {
        bool isp=true;
        int l=current.length();
        if (l<2) isp=false;
        for (int j=2;j*j<=l;j++)
            if (l%j==0) isp=false;
        if (isp) out=out+current+' ';
        current="";        
    }
    if (out.length()>0)
        out.pop_back();
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = words_in_sentence(n);
    std::cout << result << std::endl;
}
