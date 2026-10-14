class Solution:
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True

    def isParitionPalindrome(self, partitions):
        for partition in partitions:
            if not self.isPalindrome(partition):
                return False
        return True

    def recurce2(self, idx, current):
        if idx >= len(self.s):
            self.result.append(current[:])
            return
        for i in range(idx, len(self.s)):
            substr = self.s[idx : i + 1]
            if self.isPalindrome(substr):
                current.append(substr)
                self.recurce2(i + 1, current)
                current.pop()

    def palindrome_paritioning2(self, s):
        self.s = s
        idx = 0  # before this element everything is paritioned
        current = []
        self.result = []
        print(s)
        self.recurce2(idx, current)
        for partition in self.result:
            print(partition)

    def recurce(self, idx, current):
        if idx >= len(s):
            # check
            if self.isParitionPalindrome(current):
                self.result.append(current[:])
            return
        curr = self.s[idx]
        if len(current) > 0:
            # create new partition
            newCurrent = current + [curr]
            self.recurce(idx + 1, newCurrent)
            # append to to last partition
            newCurrent = current[:]
            newCurrent[-1] = newCurrent[-1] + curr
            self.recurce(idx + 1, newCurrent)
        else:
            newCurrent = current + [curr]
            self.recurce(idx + 1, newCurrent)

        return

    def palindrome_paritioning(self, s):
        self.s = s
        idx = 0  # before this element everything is paritioned
        current = []
        self.result = []
        print(s)
        self.recurce(idx, current)
        for partition in self.result:
            print(partition)


sol = Solution()
s = "aabaa"
sol.palindrome_paritioning(s)
sol.palindrome_paritioning2(s)
