class Solution:
    def add_operator_at(self, idx, s, curr):
        # base case
        if idx == len(s):
            current = "".join(curr)
            if eval(current) == self.target:
                self.result.append(current)
            return

        operators = ["+", "-", "*", ""]

        digit = s[idx]

        for opr in operators:
            last_digit = curr[-1]
            if opr != "":
                curr.append(opr)
                curr.append(digit)
            match opr:
                case "+":
                    self.add_operator_at(idx + 1, s, curr)
                case "-":
                    self.add_operator_at(idx + 1, s, curr)
                case "*":
                    self.add_operator_at(idx + 1, s, curr)
                case "":
                    if last_digit == "0":
                        continue
                    else:
                        curr[-1] += digit

                    self.add_operator_at(idx + 1, s, curr)
            if opr != "":
                curr.pop()
                curr.pop()
            else:
                curr[-1] = last_digit

    def add_operators(self, s, target):
        # operators = "*", "+", "-"

        if len(s) < 1:
            return []

        # print(s, target)
        curr = [s[0]]
        idx = 1
        self.target = target
        self.result = []
        self.add_operator_at(idx, s, curr)
        print(self.result)
        return self.result


sol = Solution()
s = "102"
target = 20
sol.add_operators(s, target)
