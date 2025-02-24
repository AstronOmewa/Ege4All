#include <bits/stdc++.h>
using namespace std;

int main(){

    fstream f("D://Ege4All/old/24/cpp/1_24.txt");

    string s;

    f >> s;

    vector<char> line(s.begin(), s.end());

    for(int i = 0; i<10000001; i++){
        line[i] = (char)(s[i]);
    }
    char * l = line.data()+1,
         * r = line.data(),
         * end_ = l + size(line)-1;
    int k = 0,
        mx = 10000001;
    for(;r<end_-1;r+=1){
        if((*r == 'T') && (*( r - 1 ) == 'T')){
            k++;
        }
        while(k>=150){
            mx = min(mx, (int)(r - l + 1));
             
            if((*l=='T')&&(*( l+1 ) == 'T')){
                k--;
            }
            l+=1;
        }
            
        }
    cout << mx;
}