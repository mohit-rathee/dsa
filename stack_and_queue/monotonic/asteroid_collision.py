from utils.stack import Stack


def sign(val):
    return val / abs(val)


class Solution:
    def asteroid_collision(self, asteroids):
        stack = Stack()
        for ast in asteroids:
            top = stack.top()
            was_equal = False
            was_smaller = False
            while top and sign(top) == 1 and sign(ast) == -1:
                if abs(top) < abs(ast):
                    stack.pop()
                    top = stack.top()
                elif abs(top) == abs(ast):
                    stack.pop()
                    top = stack.top()
                    was_equal = True
                    break
                else:
                    was_smaller = True
                    break
            if not was_equal and not was_smaller:
                stack.push(ast)

        return stack.to_list()


sol = Solution()
asteroids = [5, 10, -5, -10, 8, -8, -3, 12]
asteroids = [1, 2, 3, -4, -2]
asteroids = [10, 2, -5]
asteroids = [-10, 2, -5]

print(asteroids)
print(sol.asteroid_collision(asteroids))
