class Solution:
    def helper (self,divisor,dividend):
        if dividend<divisor:
            return 0

        # divisor * quotient + remainder = dividend
        # quotient in terms of binary(b01001) is 2^3+2^0

        i = 0
        while divisor << i <= dividend:
            i+=1
        i -= 1
        sub_quotient = divisor << i
        dividend -= sub_quotient
        return 1<<i | self.helper(divisor,dividend)

    def divide(self, divisor,dividend):
        sign = 1
        if dividend <0 and divisor > 0:
            sign = -1
        if dividend >0 and divisor < 0:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        return sign * self.helper(divisor,dividend)


sol = Solution()
print(sol.divide(3,24))
