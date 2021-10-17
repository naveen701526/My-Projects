#include<bits/stdc++.h>

using namespace std;

int main(){
    string str1;
    //Input
    getline(cin, str1);
    string str2;
    // char str2[str1.size()];
    int x=0;
    vector< int> arr;
    for(int i=0;i<str1.size();i++){
        cin >>x;
        arr.push_back(x);
    }
    //Output
    for(int i=0;i<str1.size();i++){
       str2[i] = str1[arr[i]];
    }
    for(int i=0;i<str1.size();i++) cout<<str2[i];
}
