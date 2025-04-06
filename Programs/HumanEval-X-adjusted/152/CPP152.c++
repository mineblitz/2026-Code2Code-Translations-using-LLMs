#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
#include<algorithm>
#include<stdlib.h>
vector<int> compare(vector<int> game,vector<int> guess){
    vector<int> out;
    for (int i=0;i<game.size();i++)
    out.push_back(abs(game[i]-guess[i]));
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
    string input1 = argv[2];
    if (input1.front() == '[') input1.erase(0, 1);
    if (input1.back() == ']') input1.pop_back();
    input1.erase(std::remove(input1.begin(), input1.end(), ','), input1.end());
    std::stringstream iss1( input1 );
    int myValue1;
    std::vector<int> o;
    while ( iss1 >> myValue1 )
        o.push_back( myValue1 );
    vector<int> result = compare(n, o);
    cout << "[";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            std::cout << ", ";
        }
    }
    cout << "]" << endl;
}
