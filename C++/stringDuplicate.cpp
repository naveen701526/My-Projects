#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    getline(cin, s);
    
    unordered_map<char, int> m;
    for(auto i : s){
        m[i]++;
    }
    for(auto i : s){
        if(m[i] && m[i]!=1){
            cout<<i<<','<<m[i]<<endl;
            m.erase(i);
        }
    }
    return 0;
}