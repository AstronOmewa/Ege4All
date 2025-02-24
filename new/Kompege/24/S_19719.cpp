#include <bits/stdc++.h>
using namespace std;

int main(){

    fstream f("24.12_19719.txt");
    string s;

    f >> s;
    
    vector<char> line(s.begin(), s.end());
    char * l = line.data(),
         * r = line.data(),
         * end = line.data() + line.size();
    
    int mx = 0;
    for(; r<end; ++r){
        if(*r >= '0' && *r <= '9'){
            if(r > l && *r == '0' && (r == l+1 || !isdigit(*(r-1)))){
                l = r;
            }
        }
        else if(*r == '-' || *r == '*'){
            if(r == line.data() || r == end-1 || !isdigit(*(r-1)) || !isdigit(*(r+1)) ){
                l = r+1;
            }
        }
        else{
            l = r+1;
        }

        mx = max(mx, (int)(r - l + 1));
    }
    cout << mx;
    
}