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
vector<string> words_string(string s){
    string current="";
    vector<string> out={};
    s=s+' ';
    for (int i=0;i<s.length();i++)
     if (s[i]==' ' or s[i]==',')
     {
        if (current.length()>0)
        {
            out.push_back(current);
            current="";
        }
     }
     else current=current+s[i];
     return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    vector<string> result = words_string(n);
cout << "[";
for (size_t i = 0; i < result.size(); ++i) {
result[i].erase(std::remove(result[i].begin(), result[i].end(), '\''), result[i].end());
    cout << "'" << result[i] << "'";
    if (i != result.size() - 1) {
        std::cout << ", ";
    }
}
cout << "]" << endl;
}
