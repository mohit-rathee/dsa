class Solution:
    def min_window(self, s1, s2):
        n, m = len(s1), len(s2)

        if m == 0 or m > n:
            return ""

        min_len = float("inf")
        result_start = -1
        i = 0

        while i < n:
            j = i
            count = 0

            # 1. Forward: find a complete subsequence
            while j < n:
                if s1[j] == s2[count]:
                    count += 1
                    if count == m:
                        break
                j += 1

            # No more complete subsequences exist
            # earlier loop never reach count == m
            if count < m:
                break

            end = j

            # 2. Backward: minimize this window
            count = 0
            while j >= i:
                if s1[j] == s2[m - 1 - count]:
                    count += 1
                    if count == m:
                        break
                j -= 1

            start = j

            # 3. Update the best answer
            if end - start + 1 < min_len:
                min_len = end - start + 1
                result_start = start

            # 4. Search again, allowing overlapping windows
            i = start + 1

        if result_start == -1:
            return ""

        return s1[result_start : result_start + min_len]


sol = Solution()
s1 = "abcdebdde"
s2 = "bde"
print(s1)
print(s2)
print(sol.min_window(s1, s2))
