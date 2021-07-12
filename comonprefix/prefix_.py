class Solution:
    @staticmethod
    def common_prefix(target):
        prestr =''
        sent = list(map(lambda x:list(x), target))
        for i in range(max(list(map(lambda x:len(x),sent)))):
            if(sent[j][i] != sent[j+1][i] for j in range(len(sent)-1)):
                return prestr
            else:
                prestr += sent[j][i]


if __name__ == '__main__':
    lst=["fleee","faaaow","flddd"]
    print(Solution.common_prefix(lst))
