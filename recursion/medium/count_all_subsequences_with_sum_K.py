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

    def recurse_for_K(self, index, current, current_sum):
        n = len(self.arr)

        # only when you have positive numbers
        if current_sum > self.K:
            self.skip_count += 1
            return

        if index == n:
            if current_sum == self.K:
                self.result.append(current[:])
            return

        curr = self.arr[index]
        current.append(curr)
        self.recurse_for_K(index + 1, current, current_sum + curr)
        current.pop()
        self.recurse_for_K(index + 1, current, current_sum)

    def count_all_subsequences_with_sum_K(self, arr, K):
        self.arr = arr
        self.K = K
        index = 0
        current = []
        current_sum = 0
        self.skip_count = 0
        self.result = []
        self.recurse_for_K(index, current, current_sum)
        # for i in self.result:
        #     print(i)
        print(self.skip_count)
        print(len(self.result))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [1, 2, 3]
string = "abc"
sol = Solution()
K = 10
# sol.generate_subsequences(arr)
sol.count_all_subsequences_with_sum_K(arr, K)
