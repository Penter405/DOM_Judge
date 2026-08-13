#include <bits/stdc++.h>
using namespace std;
const array<char,3> out={')',']','}'};
map<char,char> team={{')','('},{'}','{'},{']','['}};
int find(char x){
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
        if(stack.empty()){
            if(find(it)==1){
                cout<<"NO";
            return 0;
            }
            stack.push_back(it);
            continue;
        }
        if(find(it)==0){
            stack.push_back(it);
            continue;
        
        }
        if(team.at(it)==stack.back()){
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