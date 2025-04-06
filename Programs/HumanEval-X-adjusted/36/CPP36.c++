#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int fizz_buzz(int n){
    int count=0;
    for (int i=0;i<n;i++)
    if (i%11==0 or i%13==0)
    {
        int q=i;
        while (q>0)
        {
            if (q%10==7) count+=1;
            q=q/10;
        }
    } 
    return count;
}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = fizz_buzz(n);
    std::cout << result << std::endl;
}
