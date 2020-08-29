#include <iostream>
#include<vector>
using namespace std;
class Solution{
public:
    vector<vector<int >> combine(int n,int k){
        vector<vector<int >> res{};
        vector<int > path{};
        int depth =k;
        int range =n;
        back_track(res,range,1,path,depth);
    }
    void back_track(vector<vector<int >> res ,int range ,int start=1,vector<int > &path,int depth){
        if (path.size()==depth) {
            res.push_back(path);
            return ;
        }
        for (int i=start;i<=depth;i++){
            path.push_back(i);
            back_track(res,i+1,range,path,depth);
            path.pop_back();
        }

    }
};


int main()
{
//    std::cout << "Hello, World!" << std::endl;
    return 0;
}