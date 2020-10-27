#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <cassert>
using namespace std;

class Solution{
    public :

        vector<int> topKFrequent(vector<int> &nums,int k){
            assert(k>0);
            unordered_map<int,int> freq;
            for (int num:nums)
                freq[num]++;

            assert(k <=freq.size);

            set<pair<int,int>,greater<int >> record;
            

        }





}