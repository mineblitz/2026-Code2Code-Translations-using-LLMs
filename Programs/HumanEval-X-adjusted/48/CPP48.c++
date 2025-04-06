#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
bool is_palindrome(string text){
    string pr(text.rbegin(),text.rend());
    return pr==text;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    bool result = is_palindrome(n);
    std::cout << (result ? "True" : "False") << std::endl;
}
