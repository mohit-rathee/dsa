class Solution:
    def longest_unique1(self,s):
        last_seen = {}
        i = j = 0
        max_len = 0

        while j < len(s):
            char = s[j]
            if char in last_seen and last_seen[char] >= i:
                i = last_seen[char] + 1

            last_seen[char] = j
            max_len = max(max_len, j - i + 1)

            j+=1

        return max_len

    def longest_unique2(self,s):
        i = j = 0
        max_len = 0
        freq = {}
        while j<len(s):
            # print(j)
            char = s[j]
            if not freq.get(char,False):
                freq[char] = True
                max_len = max(max_len,j-i+1)
                j+=1
            else:
                while freq[s[i]]:
                    freq[s[i]] = False
                    i+=1
        return max_len


sol = Solution()
s='abcddabac' # 4
s = 'aaabbbccc' # 2
s = 'abcbcef' # 4
print(s)
print(sol.longest_unique1(s))
print(sol.longest_unique2(s))
