#include <bits/stdc++.h>
using namespace std;

int main(){
    fstream f("D:\\\\egeAll\\kompege\\24\\24.23_19887.txt");

    string s;
    f>>s;
    vector<char> line(s.begin(), s.end());

    char * l = line.data(),
         * r = line.data()+1,
         * end = line.data()+s.length();
    
    int k = 1, mx = 0;

    for(;r<end;r+=1){
        if(((int)(*(r) - '0'))%2 != ((int)(*(r-1) - '0'))%2){
            k+=1;
        }else{
            mx = max(mx, k);
            k = 1;
        }
    }

    cout << mx;

    return 0;
}