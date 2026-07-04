class Solution:
    def recurse(self, index, current):
        n = len(self.arr)
        if index == n:
            self.result.append(current[:])
            return
        current.append(self.arr[index])
        self.recurse(index + 1, current)
        current.pop()
        self.recurse(index + 1, current)

    def generate_subsequences(self, arr):
        self.arr = arr
        current = []
        index = 0
        self.result = []
        self.recurse(index, current)
        for i in self.result:
            print(i)

    def recurse_for_K(self, index, current_sum):
        n = len(self.arr)

        # only when you have positive numbers
        if current_sum > self.K:
            self.skip_count += 1
            return 0

        if index == n:
            if current_sum == self.K:
                return 1
            return 0

        curr = self.arr[index]
        take = self.recurse_for_K(index + 1, current_sum + curr)
        skip = self.recurse_for_K(index + 1, current_sum)
        return take + skip

    def count_all_subsequences_with_sum_K(self, arr, K):
        self.arr = arr
        self.K = K
        index = 0
        current_sum = 0
        self.skip_count = 0
        result = self.recurse_for_K(index, current_sum)
        # for i in self.result:
        #     print(i)
        print(result)


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [1, 2, 3]
arr = [4, 9, 2, 5, 1]
# arr = [4, 2, 10, 5, 1, 3]
# K = 5
string = "abc"
sol = Solution()
K = 10
# sol.generate_subsequences(arr)
sol.count_all_subsequences_with_sum_K(arr, K)
