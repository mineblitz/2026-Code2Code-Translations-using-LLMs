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
vector<string> sorted_list_sum(vector<string> lst){
    vector<string> out={};
    for (int i=0;i<lst.size();i++)
    if (lst[i].length()%2==0) out.push_back(lst[i]);
    string mid;
    sort(out.begin(),out.end());
    for (int i=0;i<out.size();i++)
    for (int j=1;j<out.size();j++)
    if (out[j].length()<out[j-1].length())
    {
        mid=out[j];out[j]=out[j-1];out[j-1]=mid;
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
    vector<string> result = sorted_list_sum(n);
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
