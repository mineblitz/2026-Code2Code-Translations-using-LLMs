#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
#include<stdlib.h>
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> out={};
    vector<int> has1={};
    vector<int> has2={};
    for (int i=0;i<numbers.size();i++)
    {
        if (find(has2.begin(),has2.end(),numbers[i])!=has2.end()) continue;
        if (find(has1.begin(),has1.end(),numbers[i])!=has1.end())
        {

            has2.push_back(numbers[i]);
        }
        else has1.push_back(numbers[i]);
    }
    for (int i=0;i<numbers.size();i++)
    if (find(has2.begin(),has2.end(),numbers[i])==has2.end())
        out.push_back(numbers[i]);
    return out;


}
    int main(int argc, char *argv[]) {
    string input0 = argv[1];
    if (input0.front() == '[') input0.erase(0, 1);
    if (input0.back() == ']') input0.pop_back();
    input0.erase(std::remove(input0.begin(), input0.end(), ','), input0.end());
    std::stringstream iss0( input0 );
    int myValue0;
    std::vector<int> n;
    while ( iss0 >> myValue0 )
        n.push_back( myValue0 );
    vector<int> result = remove_duplicates(n);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
