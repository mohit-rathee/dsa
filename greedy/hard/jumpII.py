class Solution:
    def standard_jumpII(self, nums):
        print(nums)
        farthest = 0
        current_end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                jumps += 1
        return jumps

    def jumpII(self, nums):
        dp = [idx + nums[idx] for idx in range(len(nums))]
        print(nums)
        i = 0
        jumps = 0
        while i < len(nums) - 1:
            jump_range = min(i + 1 + nums[i], len(nums))
            max_idx = i
            max_value = 0
            # print("range from ", i, end=" ")
            for j in range(i + 1, jump_range):
                # print((nums[j], j + nums[j]), end=" ")
                value = min(dp[j], len(nums))
                if value >= max_value:
                    max_idx = j
                    max_value = value
            # print()
            # print(nums[i], "to", nums[max_idx], "at idx", max_idx)
            # jump to this position
            i = max_idx
            jumps += 1
            # print(max_idx, jumps)

        return jumps


sol = Solution()
nums = [2, 3, 1, 1, 4]  # 2
nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]  # 3
# nums = [1, 1, 1, 1, 1, 1, 1]  # 6

# Expected output: 15
print(sol.jumpII(nums))
print(sol.standard_jumpII(nums))
