class Solution:
    def jumpI(self, nums):
        farthest = 0
        for idx in range(len(nums)):
            if idx>farthest:
                print('false')
                return False
            num = nums[idx]
            farthest = max(farthest,idx+num)
            if farthest >= len(nums)-1:
                print('turu')
                return True

sol = Solution()
nums = [2,3,1,1,4]
sol.jumpI(nums)
