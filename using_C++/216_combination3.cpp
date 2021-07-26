class Solution{
public:
    Solution(){
        for (int i=1;i<10;i++) candidates.push_back(i);
    };
    vector<vector<int >> combination (int k, int n){
        vector<int > path {};
        vector<int > visited {} ;
        backTrack(path ,visited,0,k,n);
        return res;

    }

    void backTrack(vector<int > &path,vector<int > &visited ,int start,int k,int n){
        int sum=0;
        for (auto v:path){
            sum+=v ;
        }
        if (k==path.size()) {
            if (sum == n) {
                res.push_back(path);
            }
            return;
        }
        for (int cand =start+1;cand<=9;cand++){
            if ((std::find(visited.begin(), visited.end(), cand))!=visited.end()) continue;
            visited.push_back(cand);
            path.push_back(cand);
            backTrack(path,visited,cand,k,n);
            visited.pop_back();
            path.pop_back();
        }
    }

private:
    vector<int > candidates;
    vector<vector<int>> res ;

};