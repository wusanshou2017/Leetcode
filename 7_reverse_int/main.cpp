#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int reverse_int (int target) {
        ostringstream stream;
        if (target > INT32_MAX || target < INT32_MIN) {
            return 0;
        }
        if (target >= 0) {
            stream << target;
            string str_tmp = stream.str();
            reverse(str_tmp.begin(), str_tmp.end());
            string str_res = str_tmp;
            int result = atoi(str_tmp.c_str());
            return result;
        }
        if (target < 0) {
            target = abs(target);
            stream << target;
            string str_tmp = stream.str();
            reverse(str_tmp.begin(), str_tmp.end());
            string str_res = str_tmp;
            int result = atoi(str_tmp.c_str());
            return -result;
        }
    }
};
class Solution2{
public:
    int revers_num(int target){

        if (target<10&&target>-10){
            return target;
        }
        bool is_pos_num;
        is_pos_num = target>=0?true: false;
        if (!is_pos_num){
            target=-target;
        }
        vector<int> vec_nums;
        while (target>0) {
            int temp = target %10;
            target -= temp;
            target /=10;
            vec_nums.push_back(temp);
            if (target == 0) {
                break;
            }
        }
        int res=0;

        for (int i=0;i<vec_nums.size();i++)
        {

            int add=1;
            int temp =vec_nums.size()-i-1;
            while (temp--)
            {
                add*=10;
            }
            res+=add*vec_nums[i];
        }
        return is_pos_num?res:-res ;
    }




};
int main() {
    Solution so;
    //cout<<so.reverse_int(214799999647)<<endl;
    cout<<INT32_MIN<<endl;
    cout<<INT32_MAX<<endl;

    cout<<so.reverse_int(-120)<<endl;
    Solution2 so2;
    cout<<so2.revers_num(-9953)<<endl;
    return 0;
}