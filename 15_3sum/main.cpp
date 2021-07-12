#include <iostream>
#include <vector>
#include <map>
#include<set>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int >> three_sum(vector<int > target){
        vector<vector<int >> res;
        if (target.size()<3)
        {
            return res ;
        }
        sort(target.begin(),target.end());
        int n = target.size();
        for (int i=0; i<n-2;i++)
        {

            int sum=-target[i];

            for( int j=i+1,k=n-1;j<k;)
            {
                vector <int> nums_set;


                if(target[j]+target[k]==sum)
                {
                    nums_set.push_back(target[i]);
                    nums_set.push_back(target[j]);
                    nums_set.push_back(target[k]);
                    j++;
                    k--;
                    while(target[j]==target[j+1]&&j<k)
                    {
                        j++;
                    }
                    while(target[k]==target[k+1]&&j<k)
                    {
                        k--;
                    }
                    res.push_back(nums_set);

                }
                if(target[j]+target[k]>sum)
                {
                    k--;
                }
                else if(target[j]+target[k]<sum){

                    j++;
                }
            }
            while(target[i+1]==target[i])
            {
                i++;
            }

        }
        return res;

    }


};
class Solution1{
public:
    vector< vector<int> > threeSum(vector<int> &num) {
        vector<int> numSet(3);
        vector< vector<int> > r;
        // 1.排序
        sort(num.begin(), num.end());
        int sum;
        int len = num.size();
        // 2.拿出第一个数，转化为两数和问题。注意外层循环到倒数第三个数即可
        for(int i = 0; i < len-2; i++) {
            sum = 0 - num[i];
            numSet[0] = num[i];
            // 3.两数和问题
            for(int j = i+1, k = len-1; j < k;) {
                if(num[j] + num[k] == sum) {
                    numSet[1] = num[j++];
                    numSet[2] = num[k--];
                    r.push_back(numSet);
                    // 根据题目要求，跳过重复元素
                    while(j < k && num[j] == num[j-1])
                        j++;
                    while(j < k && num[k] == num[k+1])
                        k--;
                }
                else if(num[j] + num[k] < sum)
                    j++;
                else
                    k--;
            }
            while(i < len-2 && num[i+1] == num[i])
                i++;
        }
        return r;
    }
};


int main() {
    vector <int > target{0,0,0};
    Solution so;
    vector<vector<int >>res =so.three_sum(target);
    for (auto vec :res){
        for (auto item:vec)
        {
         std::cout<<item<<" ";
        }
        std::cout<<endl;
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}