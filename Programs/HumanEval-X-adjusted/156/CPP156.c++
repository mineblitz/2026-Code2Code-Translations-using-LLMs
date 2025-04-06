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
string int_to_mini_romank(int number){
    string current="";
    vector<string> rep={"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    vector<int> num={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    int pos=0;
    while(number>0)
    {
        while (number>=num[pos])
        {
            current=current+rep[pos];
            number-=num[pos];
        }
        if (number>0) pos+=1;
    }
    return current;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    string result = int_to_mini_romank(n);
    std::cout << result << std::endl;
}
