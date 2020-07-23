using namespace std;
static const auto _ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {

        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0;i<m;i++){
            for (int j =0; j<n;j++){
                if (i ==0 && j==0) continue;
                else if (i==0 && j>0){
                    grid[i][j] = grid[i][j-1]+grid[i][j];
                }
                else if (i>0 && j==0){
                    grid[i][j] = grid[i][j]+grid[i-1][j];
                }

                else if (i>0 && j>0){
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1])+grid[i][j];
                }
            }
        }
        return grid[m-1][n-1];
    }
};