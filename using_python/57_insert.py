# 示例 1：

# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]

# 示例 2：

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
         # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)

        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output

    def my_insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        index, n = 0, len(intervals)

        start_range, end_range = newInterval

        res = []

        while index < n and intervals[index][0] < start_range:

            res.append(intervals[index])
            index += 1

        if not res or res[-1][-1] < start_range:
            res.append(newInterval)

        else:
            res[-1][-1] = max(res[-1][-1], end_range)


        while index < n:

            start, end = intervals[index]
            

            if res[-1][-1] >= start:

                res[-1][-1] = max(res[-1][-1], end)

            else:
                res.append(intervals[index])

            index += 1
            
        return res

intervals = [[1,3],[6,9]]

newInterval = [2,5]

so =Solution()

print (so.my_insert(intervals,newInterval))

