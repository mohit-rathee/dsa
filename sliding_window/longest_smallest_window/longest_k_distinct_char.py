class Solution:
    def k_distinct_chars(self, s, k):
        i = 0
        freq = {}
        max_len = 0

        for j, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1

            while len(freq) > k:
                left_char = s[i]
                freq[left_char] -= 1

                if freq[left_char] == 0:
                    del freq[left_char]

                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len


sol = Solution()
s = "aababbcaacc"  # 6
k = 2
s = "abcddefg"  # 4
k = 3
print(s)
print(k)
print(sol.k_distinct_chars(s, k))
