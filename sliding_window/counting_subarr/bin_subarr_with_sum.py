class Solution:
    def subarr_count_with_atleast_sum(self, nums, k):
        i = 0
        curr_sum = 0
        count = 0
        for j in range(len(nums)):
            # expand and update
            num = nums[j]
            curr_sum += num

            while curr_sum >= k and i <= j:
                # substr's with all end after j are valid
                count += len(nums) - j

                # shrink
                left_num = nums[i]
                curr_sum -= left_num
                i += 1
        return count

    def num_subarr_with_sum(self, nums, goal):
        count_atleast_goal = self.subarr_count_with_atleast_sum(nums, goal)
        count_atleast_goal_plus_one = self.subarr_count_with_atleast_sum(nums, goal + 1)
        # print(count_atleast_goal, count_atleast_goal_plus_one)
        return count_atleast_goal - count_atleast_goal_plus_one


sol = Solution()
nums = [1, 1, 0, 1, 0, 0, 1]  # 4
goal = 3
nums = [0, 0, 0, 0, 1]  # 10
goal = 0
print(nums, goal)
print(sol.num_subarr_with_sum(nums, goal))
