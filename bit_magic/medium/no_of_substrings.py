from time import time
import sys

sys.setrecursionlimit(10000)


class Solution:
    def recurse(self, start, curr, mask):
        # consider all options from start
        if start >= len(self.s):
            return

        char = self.s[start]
        bit = ord(char) - ord("a")

        # extend char
        curr.append(char)
        mask = mask ^ 1 << bit

        if mask == 0 or mask & (mask - 1) == 0:  # atleast one 1
            self.result.append(curr[:])

        # extend more
        self.recurse(start + 1, curr, mask)

    def count_valid_substrings(self, start):
        self.s = start
        self.result = []
        count = 0
        for start in range(len(self.s)):
            # curr = []
            mask = 0
            for end in range(start, len(self.s)):
                # consider all options from each start

                char = self.s[end]
                bit = ord(char) - ord("a")

                # extend char
                # curr.append(char)
                mask = mask ^ 1 << bit

                if mask == 0 or mask & (mask - 1) == 0:  # atleast one 1
                    # self.result.append(curr[:])
                    count += 1

        # for i in self.result:
        #     print(i)
        # print(len(self.result))
        # return len(self.result)
        print(count)
        return count

    def count_valid_substrings_brute_force(self, s):
        n = len(s)
        count = 0

        for start in range(n):
            for end in range(start, n):
                # Build the frequency of this substring
                freq = [0] * 10

                for i in range(start, end + 1):
                    idx = ord(s[i]) - ord("a")
                    freq[idx] += 1

                # Count characters with odd frequencies
                odd_count = 0
                for f in freq:
                    if f % 2 == 1:
                        odd_count += 1

                if odd_count <= 1:
                    count += 1

        print(count)
        return count

    def count_valid_substrings_optmized(self, s):
        count = 0
        mask = 0
        seen = {0: 1}  # '' is 1

        for char in s:
            # Build the frequency of this substring
            bit = ord(char) - ord("a")
            mask ^= 1 << bit
            count += seen.get(mask, 0)
            for i in range(10):  # a-j (10 char)
                count += seen.get(mask ^ 1 << i, 0)
            seen[mask] = seen.get(mask, 0) + 1

        print(count)
        return count


sol = Solution()
# input only contains character (a-j) (10 chars)
s = "aabbccddeeffgghhiijj" * 50
# s = "aabb"

start = time()
# sol.count_valid_substrings(s)
end = time()
# print(end - start)
start = end
sol.count_valid_substrings_optmized(s)
end = time()
# print(end - start)
start = end
# sol.count_valid_substrings_brute_force(s)
end = time()
# print(end - start)
