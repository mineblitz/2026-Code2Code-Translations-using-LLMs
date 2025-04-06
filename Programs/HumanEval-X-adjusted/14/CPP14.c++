#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<math.h>
#include<stdlib.h>
vector<string> all_prefixes(string str){
    vector<string> out;
    string current="";
    for (int i=0;i<str.length();i++)
    {
        current=current+str[i];
        out.push_back(current);
    }
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    vector<string> result = all_prefixes(n);
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
