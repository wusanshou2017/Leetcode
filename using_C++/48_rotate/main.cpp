#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
public:
    void rotate(vector<vector<int >> matrix){
        int n = matrix.size();
        for (int i=0;i<n;i++){
            for (int j=i;j<n;j++){
                int temp =matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] =temp;
            }
        }

        for (int i=0;i<n;i++){
          reverse (matrix[i].begin(),matrix[i].end());
        }
    }




};

int main() {

    int a =2;
    int b =3;
    a^=b^=a^=b;
    vector<int> v1{1};
    vector<int> v2{2};
    v1[0]^=v2[0]^=v1[0]^=v2[0];
    cout<<v1[0]<<endl;
    cout<<v2[0]<<endl;
    cout<<a<<endl;
    cout<<b<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}