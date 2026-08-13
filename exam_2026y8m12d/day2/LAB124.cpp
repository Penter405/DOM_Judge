#include <bits/stdc++.h>
using namespace std;
const array<char,3> out={')',']','}'};
const array<char,3> in={'(','[','{'};
map<char,char> team={{')','('},{'}','{'},{']','['}};
int find_back(char x){
    for(auto& it:out){
        if(x==it){
            return 1;
        }
    }
    return 0;
}
int main(){
    string sentence;
    vector<char> stack;
    getline(cin, sentence);
    //cout<<"done";
    for(auto& it:sentence){
        int state=0;
        for(auto& its:in){
            if(its==it){
                state=1;
            }
        }
        for(auto& its:out){
            if(its==it){
                state=1;
            }
        }
        if(state==0){
            continue;
        }
        //cout<<it<<'\n';
        /*
        for(auto& it:stack){
            cout<<it<<' ';
        }
        cout<<'\n';
        */
        if(stack.empty()){
            if(find_back(it)==1){
                cout<<"NO";
            return 0;
            }
            stack.push_back(it);
            continue;
        }
        if(find_back(it)==0){
            stack.push_back(it);
            continue;
        
        }
        if(team.at(it)==stack.back()){
            //cout<<"can close";
            stack.pop_back();
            continue;
        }else{
            cout<<"NO";
            return 0;
        }
        


    }
    if(stack.empty()){
        cout<<"YES";
    }else{
        cout<<"NO";
    }
    
    return 0;
}