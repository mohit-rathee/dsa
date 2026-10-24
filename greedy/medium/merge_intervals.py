class Solution:
    def merge_intervals(self, intervals):
        if len(intervals) == 0:
            return intervals
        for i in intervals:
            print(i)
        print()

        intervals.sort(key=lambda i: i[0])
        result = [intervals[0][:]]
        for i in range(1, len(intervals)):
            curr_s, curr_e = intervals[i]
            last_s, last_e = result[-1]
            if curr_s <= last_e:
                result[-1][0] = min(last_s, curr_s)
                result[-1][1] = max(last_e, curr_e)
            else:
                result.append(intervals[i][:])

        for i in result:
            print(i)
        return result


sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 4], [5, 6]]
sol.merge_intervals(intervals)
