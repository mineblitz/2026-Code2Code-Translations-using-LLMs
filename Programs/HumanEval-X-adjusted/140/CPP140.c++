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
string fix_spaces(string text){
    string out="";
    int spacelen=0;
    for (int i=0;i<text.length();i++)
    if (text[i]==' ') spacelen+=1;
    else
    {
        if (spacelen==1) out=out+'_';
        if (spacelen==2) out=out+"__";
        if (spacelen>2) out=out+'-';
        spacelen=0;
        out=out+text[i];
    }
    if (spacelen==1) out=out+'_';
    if (spacelen==2) out=out+"__";
    if (spacelen>2) out=out+'-';
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = fix_spaces(n);
    std::cout << result << std::endl;
}
