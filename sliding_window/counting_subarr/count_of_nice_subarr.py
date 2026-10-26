class Solution:
    def subarr_count_with_atleast_k_odd(self, nums, k):
        i = 0
        curr_odd_count = 0
        count = 0
        for j in range(len(nums)):
            # expand and update
            num = nums[j]
            if num & 1:
                curr_odd_count += 1

            while curr_odd_count >= k and i <= j:
                # substr's with all end after j are valid
                count += len(nums) - j

                # shrink
                left_num = nums[i]
                if left_num & 1:
                    curr_odd_count -= 1
                i += 1
        return count

    def no_of_odd_subarrs(self, nums, k):
        atleast_k_odds_count = self.subarr_count_with_atleast_k_odd(nums, k)
        atleast_k_plus_one_odd_count = self.subarr_count_with_atleast_k_odd(nums, k + 1)
        count_with_exactly_k_odds = atleast_k_odds_count - atleast_k_plus_one_odd_count
        return count_with_exactly_k_odds


sol = Solution()
nums = [1, 1, 2, 1, 1]  # 2
k = 3
nums = [4, 8, 2]  # 0
k = 1
print(nums, k)
print(sol.no_of_odd_subarrs(nums, k))
