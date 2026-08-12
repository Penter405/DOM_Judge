#include <bits/stdc++.h>
using namespace std;
array<int,3> guys;
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
    array<int,3> fake=format_diff(guys);
    int Anygood=0;
    
    int A=0,B=-1111,C=-1111;
    while(true){
        //under 0
        int state=1;
        /*
        for(auto& it:guys){
        cout<<it<<' ';
        }
        */
        for(auto& it:guys){
            if(it<0){
                state=0;
                break;
            }
        }
        if(state==0){
            break;
        }

        //answer
        state=1;
        fake=format_diff(guys);
        for(auto& it:fake){
            if(it!=0){
                state=0;
                break;
            }
        }
        if(state==1){
            Anygood=1;
            break;
        }


        //take off with A and take X times C with o(1)
        /*
        for(auto& it:fake){
            cout<<it<<"  ";
        }
        cout<<'\n';
        */
        if(fake[0]==0 && fake[1]%2==0 && fake[2]==3*(fake[1]/2)){
            Anygood=1;
            C=fake[1]/2;
            B=guys[0];
            break;
        }
        guys[0]-=2;guys[1]-=1;
        A+=1;
    }
    /*
    cout<<A<<' '<<B<<' '<<C<<'\n';
    cout<<A*2+B<<'\n';
    cout<<A+B+C*2<<'\n';
    cout<<B+C*3<<'\n';
    */
    if(Anygood==0){
        cout<<"NO";
    }else{
        cout<<"YES";
    }
    return 0;
}