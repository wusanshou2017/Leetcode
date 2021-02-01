#include <iostream>
#include <vector>
using namespace std;

class UnionFind{
public:
    UnionFind(int max_size):parent(vector<int >(max_size)){
        for (int i=0;i<max_size;i++){
            parent[i]=i;
            rank[i]=1 ;
        }
    }
    int find(int x){
        return parent[x]==x? x:find(parent[x]);
    }

    void to_union (int x1,int x2){
        parent[find(x1)]==find(x2);
    }
    // 判断两个元素是否在一个集合中
    bool is_same(int e1,int e2){
        return find(e1)==find(e2);
    }
    void merge(int i ,int j){
        int x =find(x),y =find(j);
        if (rank[x]<=rank[y]){
            parent[x]=y;
        }
        else{
            parent[y] =x;
        }
        if (rank[x]==rank[y] && x!=y){
            rank[y]++;
        }
    }
private:
    std::vector<int > parent;
    std::vector<int > rank;
};

int main() {

//    UnionFind ufind();
    vector<int > test_data {1,2,3,4,5,6,7};
    int n =10;
    UnionFind ufind(n);


    std::cout << "Hello, World!" << std::endl;
    return 0;
}