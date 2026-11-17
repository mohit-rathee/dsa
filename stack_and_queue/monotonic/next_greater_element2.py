from utils.stack import Stack


class Solution:
    def next_greater_el2(self, arr):
        output = [-1] * len(arr)
        stack = Stack()
        n = len(arr)
        for idx in range(2 * n - 1, -1, -1):
            el = arr[idx % n]
            top = stack.top()
            while top is not None and top <= el:
                stack.pop()
                top = stack.top()

            top = stack.top()
            if top and idx < n:
                output[idx] = top

            stack.push(el)

        return output


sol = Solution()
arr = [1, 3, 2, 4]
arr = [1, 3, 2]
arr = [6, 8, 0, 1, 3]
arr = [5, 1, 2, 3, 4]
arr = [1, 0, 0]

print(arr)
print(sol.next_greater_el2(arr))
