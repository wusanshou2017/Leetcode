#include <iostream>
#include <string>
#include <vector>
using  namespace std;
class Solution{
    public:
        vector<vector <int>> permute(vector<int> nums){
            int n = nums.size();
            if (n==0){
                return {};
            }
            vector<bool > used(n, false);
            vector<vector <int>> res;
            vector <int > path;
            dfs(nums,n,0,path,used,res);
            return res;
        }
        void dfs (vector<int> nums,int size,int depth ,vector<int > &path,vector<bool > &used ,vector<vector<int >> &res){
            if (depth== size){
                res.push_back(path);
                return ;
            }
            for (int i=0;i<size;i++){
                if (!used[i]){
                    used[i] =true;
                    path.push_back(nums[i]);
                    dfs(nums,size,depth+1,path,used,res);
                    used[i] =false;
                    path.pop_back();
                }
            }
        }
};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}