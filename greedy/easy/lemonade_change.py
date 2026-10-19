class Solution:
    def lemonade_chnage(self, bills):
        cash5 = cash10 = 0

        for bill in bills:
            if bill == 5:
                cash5 += 1
            elif bill == 10:
                if not cash5:
                    return False
                cash5 -= 1
                cash10 += 1
            else: # bill == 20:
                if cash10 and cash5:
                    cash10 -= 1
                    cash5 -= 1
                elif not cash10 and cash5>=3:
                    cash5-=3
                else:
                    return False
        return True


sol = Solution()
bills = [5, 5, 10 ,20]
print(sol.lemonade_chnage(bills))
