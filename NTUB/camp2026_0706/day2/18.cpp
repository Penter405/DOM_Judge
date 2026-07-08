#include <iostream>
#include <vector>
std::vector<int> way;
void input_vector(int size){
    //char word;
    int num;
    //int iter=0;
    for(int x=0;x<size;++x){
        std::cin>>num;
        way.push_back(num);
    }
}
int main(){
    int ever=0;
    int biggest=0;
    int size;
    std::cin>>size;
    input_vector(size);
    //std::cout<<"done";
    /*for(auto it:way){
        std::cout<<it<<' ';
    }
    */
    for(int x=0;x<size;++x){
        int now=0;
        for(int y=x;y<size;++y){
            now+=way.at(y);
            if(ever==0 || now>=biggest){
                biggest=now;
                ever=1;
            }
        }
    }
    std::cout<<biggest;
    return 0;
}
//what if we do o(n**2)
/*
8
-2 1-3 4-1 2 1-5 4
*/