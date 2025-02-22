#include <bits/stdc++.h>
using namespace std;

int f(int n){
    if(n==0){
        return 0;
    }else if(n%2 == 0){
        return f(n/8) + n%8;
    }
    return f(n/8);
}

int main(){
    int c = 0;
    for(int i=pow(8, 9);i<=pow(8, 10); i++){
        if(f(i) == 0){
            c++;
        }
    }
    cout<<c;
    return 0;
}