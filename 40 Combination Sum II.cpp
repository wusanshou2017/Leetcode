class Solution
{
  vector<vector<int>> combinationSum(vector<int> & candidates, int target)
  {  
    sort(candidates.begin(),candidates.end());
    vector<vector<int>> res;
    vector<int> combination;
    combinationSum(candidates,target, res, combination,0);
    return res;
  }
  void combinationSum(vector<int>&candidates ,int target , vector<vector<int >> res, vector<int> combination, int begin)
  {
    if(target==0)
    {
      res.push_back(combination);
      return;
    }
    else
    {
      for(int i=begin;i <candidates.size();i++ )
        {
          if(i!=begin&&candidates[i]==candidates[i-1]) continue;
          combination.push_back(candidates[i]);
          combinationSum(candidates , target-candidates[i], res, combination[i],i+1);
          combination.pop_back();
        }
    }
  
  }
}
