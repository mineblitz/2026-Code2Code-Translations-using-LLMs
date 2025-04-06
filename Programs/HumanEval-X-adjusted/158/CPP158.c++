#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#include<math.h>
#include<stdlib.h>
string find_max(vector<string> words){
    string max="";
    int maxu=0;
    for (int i=0;i<words.size();i++)
    {
        string unique="";
        for (int j=0;j<words[i].length();j++)
            if (find(unique.begin(),unique.end(),words[i][j])==unique.end())
                unique=unique+words[i][j];
        if (unique.length()>maxu or (unique.length()==maxu and words[i]<max))
        {
            max=words[i];
            maxu=unique.length();
        }
    }
    return max;
}
    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    string myValue0;
    std::vector<string> n;
    while ( iss0 >> myValue0 ){
         myValue0.erase(std::remove(myValue0.begin(), myValue0.end(), '\''), myValue0.end());   
        n.push_back( myValue0 ); }
    string result = find_max(n);
    std::cout << result << std::endl;
}
