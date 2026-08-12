#include <bits/stdc++.h>
using namespace std;
int im_correct=0;
array<int,3> guys;
set<array<int,3>> ever_different;
vector<array<int,2>> well;
array<array<int,6>,3> take={{{2,1,0,1,0},{0,2,3,0,1}}};
array<int,3> format_diff(array<int,3> me){
    int min=me[0];
    for(auto& it:me){
        if(it<min){
            min=it;
        }
    }
    for(auto& it:me){
        it-=min;
    }
    return me;
}
int recursion(array<int,3> me,array<int,2> times){
    if(im_correct==1){
        return 0;
    }
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
        im_correct=1;
        return 0;
    }
    array<int,3> fake=format_diff(me);
    if(ever_different.find(fake)!=ever_different.end()){
        return 0;
    }
    int local_correct=1;
    for(auto it: fake){
        if(it>0){
            local_correct=0;
            break;
        }

    }
    if(local_correct){
        im_correct=1;
        return 0;
    }
    ever_different.insert(fake);
    for(int x=0;x<2;++x){
        array<int,3> newme=me;
        array<int,2> newtimes=times;
        for(int y=0;y<3;++y){
            newme[y]-=take[x][y];
            
        }
        for(int y=0;y<2;++y){
            newtimes[y]+=take[x][y+3];
        }
        recursion(newme,newtimes);
    }
    return 0;
}
/*
int gets(){
    for(auto rs:well){
        if(rs[0]*2+rs[1]==guys[0] && rs[0]+rs[1]+rs[2]*2==guys[1] && rs[1]+rs[2]*3==guys[2]){
            return 1;
        }
    }
    return 0;
}
*/
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
    recursion(guys,{0,0});
    if(well.size()>0){
        cout<<"YES";
    }else{
        cout<<"NO";
    }
    return 0;
}