#include<bits/stdc++.h>
using namespace std;

void reverseArray(vector<int> &v, int start, int end){
    int temp;
    while(start<end){
        temp=v[start];
        v[start]=v[end];
        v[end]=temp;
        start++; end--;

    }
}
int main(){
    int n, ele; vector<int> vec;
    cin>>n;
    
    for(int i=0; i<n; i++){
        cin>>ele;
        vec.push_back(ele);
    }

    reverseArray(vec, 0, n-1);

    cout<<"Reversed array is: ";
    for (int i = 0; i < vec.size(); i++)
    {
        cout<<vec[i]<<" ";
    }
    
}