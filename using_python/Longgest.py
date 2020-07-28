def bucktetSort(numList, bucketNum):
    if len(numList) == 0 or len(numList) == 1:
        return numList
    maxNum = numList[0]
    minNum = numList[0]
    for i in range(1, len(numList)):   # 找到最大最小值
        if numList[i] < minNum:
            minNum = numList[i]
        elif numList[i] > maxNum:
            maxNum = numList[i]
        else:
            continue
    bucketSize = (maxNum - minNum + 1) // bucketNum   # 根据桶的数量找到每个桶的范围
    buckets = [[] for i in range(bucketNum)]
    for i in range(len(numList)):     # 将各个数分配到各个桶
        buckets[(numList[i] - minNum) // bucketSize].append(numList[i])
    for i in range(bucketNum):       # 桶内排序，可以使用各种排序方法
        buckets[i].sort()
    res = []
    for i in range(len(buckets)):   # 分别将各个桶内的数提出来，压入结果
        for j in range(len(buckets[i])):
            res.append(buckets[i][j])
    return res


numlist = [11, 34, 23, 56, 8, 20, 66, 45, 54, 87, 78]
print(bucktetSort(numlist, 5))
