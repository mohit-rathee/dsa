from utils.stack import Stack


class Solution:
    def next_greater_el(self, arr):
        output = [-1] * len(arr)
        stack = Stack()
        for el in range(len(arr) - 1, -1, -1):
            top = stack.top()
            while top is not None and top <= arr[el]:
                stack.pop()
                top = stack.top()

            if top:
                output[el] = top

            stack.push(arr[el])

        return output


sol = Solution()
arr = [1, 3, 2, 4]
arr = [1, 3, 2]
arr = [6, 8, 0, 1, 3]

print(arr)
print(sol.next_greater_el(arr))
