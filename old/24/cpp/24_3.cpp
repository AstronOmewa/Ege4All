#include <bits/stdc++.h>
using namespace std;

int main(){
    fstream f("D://Ege4All/old/24/cpp/24_58329.txt");
    string s;
    
    f>>s;
    vector<char> line(s.begin(), s.end());

    f.close();

    char * l = line.data(), * r = line.data()+2, *end = l + line.size();
    int k = 1, m = 0;
    for(;r<end;r+=1){
        if( ( (int)(*(r-2)  - '0') + (int)(*(r-1) - '0' )) > (int)(*(r)  - '0')){
            k++;
        }else{
            m = max(m, (int)(r - l + 1));
            l = r;
        }
    }
    cout<<m;
}