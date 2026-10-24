class Solution:
    def non_overlapping_intervals(self, intervals):
        intervals.sort(key=lambda i: i[1])
        # for i in intervals:
        #     print(i)
        count = 0
        last_end = float('-inf')
        for i in intervals:
            start,end = i
            # print(start,last_end)
            if start >= last_end:# overlapping intervals
                last_end = end
                count+=1
        print(len(intervals)-count)
        return len(intervals)-count


sol = Solution()
intervals = [ [1, 2] , [2, 3] , [3, 4] ,[1, 3] ]
intervals = [ [1, 3] , [1, 4] , [3, 5] , [3, 4] , [4, 5] ]
intervals = [ [1, 10] , [1, 4] , [3, 8] , [3, 4] , [4, 5] ]
sol.non_overlapping_intervals(intervals)
