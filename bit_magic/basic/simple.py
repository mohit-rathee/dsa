class Solution:
    def is_ith_bit_set(self, num, i):
        print(bin(num), i)
        # num_with_ith_bit_set = 1 << i
        # print(bin(num_with_ith_bit_set))
        if num & 1 << i:
            print("true")
            return True
        print("false")
        return False

    def is_odd(self, num):
        is_odd = num & 1
        print(is_odd)
        return is_odd

    def swap_num(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        print(a, b)
        return a, b

    def set_rightmost_0(self, num):
        # num = 11 (b1011), num-1 = 12 (b1100)
        # 1100 & 1011 ==> 1000
        num = num | num + 1
        print(bin(num))
        return num

    def unset_rightmost_1(self, num):
        # num = 12 (b1100), num-1 = 11 (b1011)
        # 1100 & 1011 ==> 1000
        return num & num - 1

    def is_power_of_2(self, num):
        if num == 0:
            return False
        num = self.unset_rightmost_1(num)
        if num == 0:
            return True
        else:
            return False

    def count_set_bits(self, num):
        count = 0
        print(bin(num))
        while num:
            num = self.unset_rightmost_1(num)
            count += 1
        print(count)
        return count


sol = Solution()
sol.is_ith_bit_set(12, 1)
sol.swap_num(1, 2)
sol.is_odd(5)
sol.is_power_of_2(16)
sol.set_rightmost_0(13)
sol.count_set_bits(19)
