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


sol = Solution()
arr = [2,3,6,7]
K = 7
sol.combinantion_sum_I(arr, K)
print()
arr = [10, 1, 2, 7, 6, 1, 5]
K = 8
sol.combinantion_sum_II(arr, K)
