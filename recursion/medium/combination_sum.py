class Solution:
    def recurse_I(self, idx, current, current_sum):
        if current_sum == self.K:
            self.result.append(current[:])
            return

        n = len(self.arr)
        if current_sum > self.K or idx == n:
            return

        curr_val = self.arr[idx]

        # picking more than once
        current.append(curr_val)
        current_sum += curr_val
        self.recurse_I(idx, current, current_sum)

        # skip
        current.pop()
        current_sum -= curr_val
        self.recurse_I(idx + 1, current, current_sum)

    def combinantion_sum_I(self, arr, K):
        self.arr = arr
        self.K = K
        index = 0
        current = []
        current_sum = 0
        self.result = []
        self.recurse_I(index, current, current_sum)
        for ans in self.result:
            print(ans)

    def recurse_II(self, idx, current, current_sum):
        if current_sum == self.K:
            self.result.append(current[:])
            return

        n = len(self.arr)
        if current_sum > self.K or idx == n:
            return

        for i in range(idx, n):
            if i > idx and self.arr[i] == self.arr[i - 1]:
                continue
            curr_val = self.arr[i]
            # picking more than once
            current.append(curr_val)
            current_sum += curr_val
            self.recurse_II(i + 1, current, current_sum)
            # skip this element
            current.pop()
            current_sum -= curr_val

    def combinantion_sum_II(self, arr, K):
        self.arr = sorted(arr)
        self.K = K
        index = 0
        current = []
        current_sum = 0
        self.result = []
        self.recurse_II(index, current, current_sum)
        for ans in self.result:
            print(ans)

    def recurse_III(self, n, idx, current, currentSum):
        if currentSum == self.k and n == 0:
            self.result.append(current[:])
            return
        if idx == len(self.arr) or n == 0 or currentSum > self.k:
            return
        curr = self.arr[idx]
        # take it
        current.append(curr)
        self.recurse_III(n - 1, idx + 1, current, currentSum + curr)
        # skip it
        current.pop()
        self.recurse_III(n, idx + 1, current, currentSum)

    def combinantion_sum_III(self, k, n):
        # repeated selection not allowed
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.result = []
        current = []
        currentSum = 0
        idx = 0
        self.k = k
        self.recurse_III(n, idx, current, currentSum)
        for ans in self.result:
            print(ans)

    def recurse_IV(self, n, idx, current, currentSum):
        if currentSum == self.k and n == 0:
            self.result.append(current[:])
            return
        if idx == len(self.arr) or n == 0 or currentSum > self.k:
            return
        curr = self.arr[idx]
        # take it
        current.append(curr)
        self.recurse_IV(n - 1, idx, current, currentSum + curr)
        # skip it
        current.pop()
        self.recurse_IV(n, idx + 1, current, currentSum)

    def combinantion_sum_IV(self, k, n):
        # repeated selection are allowed
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.result = []
        current = []
        currentSum = 0
        idx = 0
        self.k = k
        self.recurse_IV(n, idx, current, currentSum)
        for ans in self.result:
            print(ans)


sol = Solution()
arr = [2, 3, 6, 7]
K = 7
sol.combinantion_sum_I(arr, K)
print()
arr = [10, 1, 2, 7, 6, 1, 5]
K = 8
sol.combinantion_sum_II(arr, K)
print()
k = 14
n = 4
sol.combinantion_sum_III(k, n)
print()
k = 14
n = 2
sol.combinantion_sum_IV(k, n)
