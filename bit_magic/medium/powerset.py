class Solution:
    def powerset(self, arr):
        no_of_subsets = 1<<len(arr)
        result = []
        def is_ith_bit_set(num,i):
            return num & 1<<i
        for sub in range(no_of_subsets):
            subset = []
            for idx in range(len(arr)):
                if is_ith_bit_set(sub,idx):
                    subset.append(arr[idx])
            result.append(subset)
        print(result)
        return result


sol = Solution()
arr = [1,2,3]
sol.powerset(arr)
