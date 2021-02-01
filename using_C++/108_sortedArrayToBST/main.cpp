#include <iostream>
#include <vector>
using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x):val(x),left(NULL),right(NULL){}
};
//[-10,-3,0,5,9] l:0,r:4
//[0,-10,-3,5,9]
class Solution{
public:
    TreeNode *helper(int left ,int right,vector<int >& nums){
        if (left>right) return NULL;
        int mid = (left+right)/2; // 2
        cout <<"the_mid:.."<<mid<<endl;
        TreeNode *root =new TreeNode(nums[mid]);
        root->left = helper(left,mid-1,nums); // (0,1)
        root->right = helper(mid+1,right ,nums);// (3,4)
        return root;
    }

    TreeNode *sortedArrayToBST (vector<int> &nums) {
        return helper(0, nums.size() - 1, nums);
    }
};

int main() {
    int x =(0+1)/2;
    cout<<x<<endl;
    Solution so;
    vector<int> data_test{-10,-3,0,5,9};
    so.sortedArrayToBST(data_test);
    std::cout << "Hello, World!" << std::endl;
    return 0;
}