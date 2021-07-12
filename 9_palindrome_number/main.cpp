#include <iostream>
#include <vector>
using namespace std;
class Solution{
public:
    bool is_palindrome_number(int target) {
        if (target > 0 && target < 10) {
            return true;
        }
        if (target < 0) {
            return false;
        }
        vector<int> vec_nums;
        while (target > 0){
            int tmp=target%10;
            target-=tmp;
            vec_nums.push_back(tmp);
            target/=10;
        }

        for (int start=0,end=vec_nums.size()-1;start<end;start++,end--){
            if (vec_nums[start]!=vec_nums[end]){
                return false;
            }
        }
        return true;
    }
};
int main() {
    Solution so;
    if (so.is_palindrome_number(19999))
        std::cout << "Hello, World!" << std::endl;
    return 0;
}