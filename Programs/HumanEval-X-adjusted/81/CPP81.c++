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
vector<string> numerical_letter_grade(vector<float> grades){
    vector<string> out={};
    for (int i=0;i<grades.size();i++)
    {
        if (grades[i]>=3.9999) out.push_back("A+");
        if (grades[i]>3.7001 and grades[i]<3.9999) out.push_back("A");
        if (grades[i]>3.3001 and grades[i]<=3.7001) out.push_back("A-");
        if (grades[i]>3.0001 and grades[i]<=3.3001) out.push_back("B+");
        if (grades[i]>2.7001 and grades[i]<=3.0001) out.push_back("B");
        if (grades[i]>2.3001 and grades[i]<=2.7001) out.push_back("B-");
        if (grades[i]>2.0001 and grades[i]<=2.3001) out.push_back("C+");
        if (grades[i]>1.7001 and grades[i]<=2.0001) out.push_back("C");
        if (grades[i]>1.3001 and grades[i]<=1.7001) out.push_back("C-");
        if (grades[i]>1.0001 and grades[i]<=1.3001) out.push_back("D+");
        if (grades[i]>0.7001 and grades[i]<=1.0001) out.push_back("D");
        if (grades[i]>0.0001 and grades[i]<=0.7001) out.push_back("D-");
        if (grades[i]<=0.0001) out.push_back("E");
    }
    return out;
}
    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    float myValue0;
    std::vector<float> n;
    while ( iss0 >> myValue0 )
        n.push_back( myValue0 );
    vector<string> result = numerical_letter_grade(n);
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
