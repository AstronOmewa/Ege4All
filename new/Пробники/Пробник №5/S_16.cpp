#include <bits/stdc++.h>
using namespace std;

long long f(long long n){
    if(n<=3) return n-1;
    if((n%2)==0) return f(n - 2) + n / 2 - f(n - 4);
    else return f(n - 1)*n + f(n - 2);
}

int main(){
    cout<<f(4952) + 2*f(4958) + f(4964);
    return 0;
}