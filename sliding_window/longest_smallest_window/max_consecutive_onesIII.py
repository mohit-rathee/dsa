class Solution:
    def longest_ones(self, nums,k):
        # after flipping k 0's to 1 we need longest count for 1.
        # we can simply find longest substr with atmost two 0's.

        i = j = 0
        zero_count = 0
        max_len = 0
        while j < len(nums):
            el = nums[j]
            if el == 0:
                zero_count += 1
                if zero_count > k:
                    # shrink
                    while nums[i] != 0:
                        i += 1
                    zero_count -= 1
                    i+= 1
            max_len = max(max_len,j-i+1)

            j+=1

        return max_len

    
    def longest_ones2(self, nums, k):
        i = j = 0
        zero_count = 0
        max_len = 0

        while j< len(nums):
            # expand
            if nums[j] == 0:
                zero_count += 1

            if zero_count > k:
                # shrink by one only, keeping the size of window to max
                if nums[i] == 0:
                    zero_count -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

            j+=1

        return max_len


sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] # 10
k = 3
nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] # 9
k = 3
print(nums)
print(k)
print(sol.longest_ones(nums,k))
print(sol.longest_ones2(nums,k))
