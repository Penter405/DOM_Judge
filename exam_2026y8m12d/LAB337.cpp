#include <bits/stdc++.h>
using namespace std;
array<int,3> guys;
set<array<int,3>> ever;
vector<array<int,3>> well;
array<array<int,6>,3> take={{{2,1,0,1,0,0},{1,1,1,0,1,0},{0,2,3,0,0,1}}};
int recursion(array<int,3> me,array<int,3> times){
    int good=1;
    for(auto& it:me){
        //cout<<it;
        if(it<0){
            good=-1;
            break;
        }
        if(it>0){
            good=0;
        }
    }
    //cout<<'\n';
    if(good==-1){
        return 0;
    }else if(good==1){
        well.push_back(times);
        return 0;
    }

    if(ever.find(times)!=ever.end()){
        return 0;
    }

    ever.insert(times);
    for(int x=0;x<3;++x){
        array<int,3> newme=me;
        array<int,3> newtimes=times;
        for(int y=0;y<3;++y){
            newme[y]-=take[x][y];
            newtimes[y]+=take[x][y+3];
        }
        recursion(newme,newtimes);
    }
    return 0;
}
int gets(){
    for(auto rs:well){
        if(rs[0]*2+rs[1]==guys[0] && rs[0]+rs[1]+rs[2]*2==guys[1] && rs[1]+rs[2]*3==guys[2]){
            return 1;
        }
    }
    return 0;
}
int main(){
    for(int x=0;x<3;++x){
        int bot;
        //cout<<"input:";
        cin>>bot;
        if(x==3){
            cout<<"wrong";
        }
        guys[x]=bot;
    }
    recursion(guys,{0,0,0});
    if(gets()==1){
        cout<<"YES";
    }else{
        cout<<"NO";
    }
    return 0;
}