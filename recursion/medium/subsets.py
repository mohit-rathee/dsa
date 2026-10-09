class Solution:
    def recurse_I(self, idx, current_sum):
        if idx == len(self.arr):
            self.result.append(current_sum)
            return
        # take it
        self.recurse_I(idx + 1, current_sum + self.arr[idx])
        # skip it
        self.recurse_I(idx + 1, current_sum)

    def subset_I(self, arr):
        self.arr = arr
        index = 0
        current_sum = 0
        self.result = []
        self.recurse_I(index, current_sum)
        for ans in self.result:
            print(ans)

    def recurse_II(self, idx, current):
        n = len(self.arr)

        # base case
        self.result.append(current[:])

        for i in range(idx, n):
            if i > idx and self.arr[i] == self.arr[i - 1]:
                # skip duplicate sibling branches
                continue
            # take it,
            curr = self.arr[i]
            current.append(curr)
            self.recurse_II(i + 1, current)
            # skip it
            current.pop()

    def subset_II(self, arr):
        self.arr = sorted(arr)
        index = 0
        self.result = []
        current = []
        self.recurse_II(index, current)
        for ans in self.result:
            print(ans)


sol = Solution()
arr = [2, 3]
sol.subset_I(arr)
print()
arr = [1, 2, 2]
K = 8
sol.subset_II(arr)
