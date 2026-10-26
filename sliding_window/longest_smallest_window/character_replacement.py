class Solution:
    def char_replacement(self, s, k):
        i = j = 0
        max_len = 0
        freq = {}
        max_freq = 0
        while j < len(s):
            char = s[j]
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            while j - i + 1 - max_freq > k:
                # shrink
                left_char = s[i]
                freq[left_char] -= 1
                if freq[left_char] == 0:
                    del freq[left_char]
                i += 1

            max_len = max(max_len, j - i + 1)
            # print(i, j, freq, j - i + 1, max_len)
            j += 1
        return max_len


sol = Solution()
s = "BAABAABBBAAA"
k = 2
print(s)
print(k)
print(sol.char_replacement(s, k))
