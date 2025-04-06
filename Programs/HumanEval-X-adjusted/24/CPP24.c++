#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int largest_divisor(int n){
    for (int i=2;i*i<=n;i++)
        if (n%i==0) return  n/i;
    return 1;

}
    int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int result = largest_divisor(n);
    std::cout << result << std::endl;
}
