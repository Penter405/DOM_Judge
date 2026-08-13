#include <bits/stdc++.h>
using namespace std;


int main(){
    int need;
    cin>>need;
    vector<int> stair(need+1,0);
    stair[0]=1;
    array<int,2> climb={1,2};
    //for(auto& it:stair){
    //    cout<<it;
    //}
    //cout<<'\n';
    for(int x=1;x<need+1;++x){
        int me=0;
        for(auto cl:climb){
            if(x-cl>=0){
                me+=stair[x-cl];
            }
        }
        stair[x]=me;
    }
    cout<<stair[need];
    return 0;
}