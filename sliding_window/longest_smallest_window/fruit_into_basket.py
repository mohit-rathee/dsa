class Solution:
    def total_fruits(self, fruits):
        # find the longest subarr with at most 2 unique char
        i = j = 0
        freq = {}
        max_fruits = 0
        while j < len(fruits):
            fruit = fruits[j]
            freq[fruit] = freq.get(fruit, 0) + 1
            if len(freq) > 2:
                while len(freq) > 2:
                    left_fruit = fruits[i]
                    if freq[left_fruit] > 1:
                        freq[left_fruit] -= 1
                    else:
                        del freq[left_fruit]
                    i += 1
            max_fruits = max(max_fruits, j - i + 1)
            j += 1
        return max_fruits


sol = Solution()
fruits = [1, 2, 1]  # 3
fruits = [1, 2, 3, 2, 2]  # 4
fruits = [1, 0, 1, 4, 1, 4, 1, 2, 3]  # 5
print(fruits)
print(sol.total_fruits(fruits))
