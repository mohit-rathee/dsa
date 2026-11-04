from utils.stack import Stack


class Solution:
    def is_valid(self, s):
        stack = Stack()
        pair = {"(": ")", "[": "]", "{": "}"}
        reverse_pair = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in pair:
                stack.push(char)
            elif char in reverse_pair:
                if stack.top() == reverse_pair[char]:
                    stack.pop()
                else:
                    return False

        return stack.is_empty()


sol = Solution()
s = "()[{}()]"
print(s)
print(sol.is_valid(s))
