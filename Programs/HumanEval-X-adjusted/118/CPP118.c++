#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<algorithm>
using namespace std;
#include<stdlib.h>
string get_closest_vowel(string word){
    string out="";
    string vowels="AEIOUaeiou";
    for (int i=word.length()-2;i>=1;i-=1)
        if (find(vowels.begin(),vowels.end(),word[i])!=vowels.end())
            if (find(vowels.begin(),vowels.end(),word[i+1])==vowels.end())
                if (find(vowels.begin(),vowels.end(),word[i-1])==vowels.end())
                    return out+word[i];
    return out;
}
    int main(int argc, char *argv[]) {
    string n = argv[1];
    string result = get_closest_vowel(n);
    std::cout << result << std::endl;
}
