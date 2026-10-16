class Solution:
    def add_operator_at(self, idx, s, curr, curr_val, last_operand, factor):
        # Base case
        if idx == len(s):
            current = "".join(curr)
            if curr_val == self.target:
                self.result.append(current)
            return

        digit = s[idx]
        num = int(digit)

        # 1. Addition
        curr.extend(["+", digit])
        self.add_operator_at(idx + 1, s, curr, curr_val + num, num, 1)
        curr.pop()
        curr.pop()

        # 2. Subtraction
        curr.extend(["-", digit])
        self.add_operator_at(idx + 1, s, curr, curr_val - num, -num, -1)
        curr.pop()
        curr.pop()

        # 3. Multiplication
        curr.extend(["*", digit])
        new_operand = last_operand * num
        new_value = curr_val - last_operand + new_operand

        self.add_operator_at(idx + 1, s, curr, new_value, new_operand, last_operand)
        curr.pop()
        curr.pop()

        # 4. Concatenation
        last_number = curr[-1]

        # Prevent leading zeros, e.g. "05"
        if last_number == "0":
            return

        new_number = int(last_number + digit)

        # Replace the previous operand with the extended number.
        new_operand = factor * new_number
        new_value = curr_val - last_operand + new_operand

        curr[-1] += digit
        self.add_operator_at(idx + 1, s, curr, new_value, new_operand, factor)
        curr[-1] = last_number

    def add_operators(self, s, target):
        if not s:
            return []

        self.target = target
        self.result = []

        first = int(s[0])
        self.add_operator_at(1, s, [s[0]], first, first, 1)

        print(self.result)
        return self.result


class Solution2:
    def addOperators(self, s: str, target: int) -> list[str]:
        result = []
        n = len(s)

        def backtrack(idx, expr, value, last_operand):
            if idx == n:
                if value == target:
                    result.append(expr)
                return

            for end in range(idx, n):
                # Numbers cannot have leading zeros.
                if end > idx and s[idx] == "0":
                    break

                num = int(s[idx : end + 1])
                text = s[idx : end + 1]

                if idx == 0:
                    # First number: no operator before it.
                    backtrack(end + 1, text, num, num)
                else:
                    # Addition
                    backtrack(end + 1, expr + "+" + text, value + num, num)

                    # Subtraction
                    backtrack(end + 1, expr + "-" + text, value - num, -num)

                    # Multiplication: correct operator precedence.
                    backtrack(
                        end + 1,
                        expr + "*" + text,
                        value - last_operand + last_operand * num,
                        last_operand * num,
                    )

        backtrack(0, "", 0, 0)
        print(result)
        return result


s = "1234"
target = 33

sol = Solution()
sol.add_operators(s, target)

sol = Solution2()
sol.addOperators(s, target)
