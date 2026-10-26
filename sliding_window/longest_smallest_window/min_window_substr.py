class Solution:
    def min_window(self, s, t):
        req_freq = {}
        for char in t:
            req_freq[char] = req_freq.get(char, 0) + 1
        i = j = 0
        min_len = float("inf")
        rng = [-1, -1]
        freq = {}

        formed = 0
        required = len(req_freq)

        while j < len(s) and i < len(s):
            char = s[j]
            if char in req_freq:
                freq[char] = freq.get(char, 0) + 1
                if freq[char] == req_freq[char]:
                    formed += 1
            while formed == required:
                if min_len > j - i + 1:
                    min_len = j - i + 1
                    rng[0] = i
                    rng[1] = j
                left_char = s[i]
                if left_char in req_freq:
                    freq[left_char] -= 1
                    if freq[left_char] < req_freq[left_char]:
                        formed -= 1
                    if freq[left_char] == 0:
                        del freq[left_char]

                i += 1

            j += 1

        x, y = rng
        if x == -1 and y == -1:
            return ""

        return s[x : y + 1]


sol = Solution()
s = "ACDBCAB"  # 2 AB
t = "AB"
# s = "ADOBECODEBANC"  # 4 BANC
# t = "ABC"
print(s)
print(t)
print(sol.min_window(s, t))
