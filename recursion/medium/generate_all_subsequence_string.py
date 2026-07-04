from datetime import datetime


class Solution:
    def generate_all_subsequence_string(self, s):
        if len(s) == 1:
            return [s]
        first_char = s[0]
        subsequences = self.generate_all_subsequence_string(s[1:])
        return (
            subsequences
            + [first_char + sub_seq for sub_seq in subsequences]
            + [first_char]
        )

    def count_all_subsequence_string(self, n):
        if n == 1:
            return 1
        prev_count = self.count_all_subsequence_string(n - 1)
        return (2 * prev_count) + 1

    def count_all_subsequence_string_by_iteration(self, s):
        n = len(s)
        count = 0
        for _ in range(n):
            count *= 2
            count += 1
        return count

    # Function to return all subsequences of string s
    def generate_all_subsequence_string_by_binary(self, s):
        n = len(s)

        total = 1 << n
        subsequences = []
        for mask in range(total):
            subseq = []
            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])

            subsequences.append("".join(subseq))
        return subsequences[1:]

    def just_count_all_subsequence_string(self, s):
        return self.count_all_subsequence_string(len(s))


sol = Solution()
s = "abcdef"
ans = sol.generate_all_subsequence_string(s)
print(ans)
ans = sol.generate_all_subsequence_string_by_binary(s)
print(ans)
ans = sol.just_count_all_subsequence_string(s)
print(ans)
ans = sol.count_all_subsequence_string_by_iteration(s)
print(ans)
