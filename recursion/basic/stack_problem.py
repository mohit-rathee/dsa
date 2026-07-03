from utils.stack import Stack


class Solution:
    def insert_at_bottom(self, stack, val):
        if stack.is_empty():
            stack.push(val)
            # print("push", val, stack)
        else:
            top = stack.pop()
            # print("pop", top, stack)
            self.insert_at_bottom(stack, val)
            stack.push(top)
            # print("push", top, stack)

    def insert_in_sorted(self, stack, val):
        if stack.is_empty():
            stack.push(val)
        else:
            top = stack.top()
            if top < val:
                stack.push(val)
            else:
                top = stack.pop()
                self.insert_in_sorted(stack, val)
                stack.push(top)

    def sort_stack(self, stack):
        # print(stack)
        if stack.is_empty():
            return
        top = stack.pop()
        self.sort_stack(stack)
        self.insert_in_sorted(stack, top)
        # print(stack)

    def reverse_stack(self, stack):
        if not stack.is_empty():
            top = stack.pop()
            # print("pop", top)
            self.reverse_stack(stack)
            # print("insert_at_bottom", stack, top)
            self.insert_at_bottom(stack, top)
            # print(stack)


sol = Solution()
stack = Stack([1, 0, 2, 3, 4, 5])
print(stack)
sol.reverse_stack(stack)
print(stack)
sol.sort_stack(stack)
print(stack)
