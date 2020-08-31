#include <iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int >> res{};
        vector<int > path{};
        int depth =k;
        int range =n;
        back_track(res,n,path,depth,1);
        return res ;
    }
    void back_track(vector<vector<int >> &res ,int range ,vector<int > &path,int depth,int start=1){
        if (path.size()==depth) {
            res.push_back(path);
            return ;
        }
        for (int i=start;i<=depth;i++){
            path.push_back(i);
            back_track(res,range,path,depth,i+1);
            path.pop_back();
            for (auto num:path){
                cout<<num<<endl;
            }
        }

    }
};


int main()
{
//    std::cout << "Hello, World!" << std::endl;
    Solution so;
    vector<vector<int >> res =so.combine(4,2);
    for(auto vec:res){
        for(auto num:vec){

            cout<<num<<",";
        }
        cout<<endl;
    }

    return 0;
}