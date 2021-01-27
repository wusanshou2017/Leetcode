#include <iostream>
#include <vector>
using namespace std;

class UnionFind{
public:
    UnionFind(int max_size):parent(vector<int >(max_size)){
        for (int i=0;i<max_size;i++){
            parent[i]=i;
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
private:
    std::vector<int > parent;
};

int main() {

    UnionFind ufind();
    vector<int > test_data {1,2,3,4,5,6,7};


    std::cout << "Hello, World!" << std::endl;
    return 0;
}