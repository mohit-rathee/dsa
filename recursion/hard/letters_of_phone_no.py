class Solution:
    map = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def helper(self, idx, current, s):
        if idx == len(s):
            return current
        key = s[idx]
        letters = self.map[key]
        new_current = []
        for curr in current:
            for letter in letters:
                new_current.append(curr + letter)
        current = new_current
        return self.helper(idx + 1, current, s)

    def letters_of_phone_no(self, s):
        if not s:
            return []

        idx = 0
        result = self.helper(idx, [""], s)
        for i in result:
            print(i)


sol = Solution()
s = "68"
sol.letters_of_phone_no(s)
