#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
#include<algorithm>
#include<stdlib.h>
vector<string> odd_count(vector<string> lst){
    vector<string> out={};
    for (int i=0;i<lst.size();i++)
        {
            int sum=0;
            for (int j=0;j<lst[i].length();j++)
                if (lst[i][j]>=48 and lst[i][j]<=57 and lst[i][j]%2==1)
                sum+=1;
            string s="the number of odd elements in the string i of the input.";
            string s2="";
            for (int j=0;j<s.length();j++)
                if (s[j]=='i') s2=s2+to_string(sum);
                else s2=s2+s[j];
            out.push_back(s2);
        }
    return out;
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
    vector<string> result = odd_count(n);
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
