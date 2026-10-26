class Solution:
    def subarr_with_atleast_k_distinct(self, nums, k):
        i = 0
        freq = {}
        count = 0
        for j in range(len(nums)):
            # expand and update
            num = nums[j]
            freq[num] = freq.get(num, 0) + 1

            while len(freq) >= k and i <= j:
                # substr's with all end after j are valid
                count += len(nums) - j

                # shrink
                left_num = nums[i]
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]

                i += 1
        return count

    def subarr_with_k_distinct(self, nums, k):
        cnt_with_atleast_k = self.subarr_with_atleast_k_distinct(nums, k)
        cnt_with_atleast_k_plus_one = self.subarr_with_atleast_k_distinct(nums, k + 1)
        return cnt_with_atleast_k - cnt_with_atleast_k_plus_one

    # Counts subarrays having
    # at most limit distinct values.
    def count_at_most(self, nums, k):
        # No non-empty subarray
        # can satisfy this limit.
        if k <= 0:
            return 0

        frequency = {}

        left = 0
        count = 0

        # Expand the window with right.
        for right in range(len(nums)):
            value = nums[right]

            frequency[value] = frequency.get(value, 0) + 1

            # Shrink until the window
            # has at most limit values.
            while len(frequency) > k:
                left_value = nums[left]
                frequency[left_value] -= 1

                # Remove the value only
                # after its last copy leaves.
                if frequency[left_value] == 0:
                    del frequency[left_value]

                left += 1

            # Every start from left to right
            # forms a valid subarray.
            count += right - left + 1

        return count

    # Counts subarrays containing
    # exactly k distinct integers.
    def subarr_with_k_distinct2(self, nums, k):
        # Exactly k distinct values
        # require a positive k.
        if k <= 0:
            return 0

        return self.count_at_most(nums, k) - self.count_at_most(nums, k - 1)


sol = Solution()
nums = [1, 2, 1, 2, 3]  # 7
k = 2
nums = [1, 2, 1, 3, 4]  # 3
k = 3
print(nums, k)
print(sol.subarr_with_k_distinct(nums, k))
print(sol.subarr_with_k_distinct2(nums, k))
