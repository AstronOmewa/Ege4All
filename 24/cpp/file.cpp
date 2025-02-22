#include <bits/stdc++.h>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

int main(){
    ifstream f("D://egeAll/24/cpp/24.txt");
    
    string s;
    
    f>>s;
    char line[1100000-1];
    for(int i=0;i<1100000;i++){
        line[i]=(char)(s[i]);
    }

    f.close();

    char * l = &line[0];
    char * r = &line[0];
    char * end = l + (size(line));
    int ke = 0,
        ka = 0,
        m = 0;

    int cnt = 0, mx = 0, k = 0;
    string a = "a";
    for(;r!=end; r+=1){
        if(*r == 'E'){ ke++;}
        if(*r == 'A'){
            if(ke >= 3){ mx = max(mx, (int)((r - l - 1)/(size(a))));}
            l = r;
        }
    }
    cout<<mx;
    return 0;
}