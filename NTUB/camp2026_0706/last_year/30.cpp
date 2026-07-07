#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>
std::unordered_map<char,std::vector<char>> walk;
std::unordered_map<char,char> back;
std::map<char,int> answer;
int dfs(char root){
    int result=0;
    for(auto it :walk[root]){
        result+=dfs(it);
    }
    answer[root]=result;
    return 1+result;

}
char get_root(char x){
    while(back.find(x)!=back.end()){
        x=back[x];
    }
    return x;
}
int main(){
    int x;
    char could='-';
    std::cin>>x;
    for(int y=0;y<x;++y){
        char a,b;
        std::cin>>a>>b;
        if(walk.find(a)==walk.end()){
            std::vector<char> bot;
            walk[a]=bot;
        }
        walk[a].push_back(b);
        back[b]=a;
        if(could=='-'){
            could=a;
        }

    }
    dfs(get_root(could));
    for(auto it:answer){
        std::cout<<it.first<<' '<<it.second<<'\n';
    }
    return 0;
}