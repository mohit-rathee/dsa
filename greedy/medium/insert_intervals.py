class Solution:
    def insert_intervals2(self, intervals, newInterval):
        result = []
        start, end = newInterval

        for s, e in intervals:
            if e < start:
                result.append([s, e])

            elif s > end:
                result.append([start, end])
                start, end = s, e

            else:
                start = min(start, s)
                end = max(end, e)

        result.append([start, end])

        for i in result:
            print(i)

        return result

    def insert_intervals(self, intervals, newInterval):

        for i in intervals:
            print(i, end=" ")

        print()
        print(newInterval)
        print()

        result = []
        i = 0
        n = len(intervals)

        # 1. Add intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # 3. Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        for i in result:
            print(i)

        return result


sol = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [11, 12]]
newInterval = [4, 8]
intervals = [[1, 2], [3, 4], [7, 8], [9, 10]]
newInterval = [5, 6]
sol.insert_intervals(intervals, newInterval)
sol.insert_intervals2(intervals, newInterval)
