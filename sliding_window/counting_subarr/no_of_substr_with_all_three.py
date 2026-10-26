class Solution:
    def number_of_substrings(self, s):
        characters = "abc"
        i = j = 0
        count = 0
        freq = [0 for _ in range(len(characters))]

        for j in range(len(s)):
            char = s[j]
            # expand & update
            idx = ord(char) - ord("a")
            freq[idx] += 1

            while 0 not in freq:
                # valid
                # substr's s[i:j..end] are all valid (end = len(s)-1)
                count += len(s) - j
                # shrink
                left_char = s[i]
                left_idx = ord(left_char) - ord("a")
                freq[left_idx] -= 1
                i += 1

        return count


sol = Solution()
s = "abcba"  # 5
s = "ccabcc"  # 8
print(s)
print(sol.number_of_substrings(s))
