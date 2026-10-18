class Solution:
    def singleI(self, arr):
        ans = 0
        for el in arr:
            ans = ans^el
        print(ans)
        return ans

    def singleII(self,arr):
        ones = twos = 0
        for num in arr:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        print(ones)
        return ones

    def singleIII(self,arr):
        xor  = 0
        for num in arr:
            xor ^= num
        print(bin(xor))
        # take the index of rightmost set bit
        idx = (xor & -xor).bit_length() -1

        def is_ith_bit_set(num,i):
            return num & 1<<i 

        bucket1 = bucket2 = 0

        for num in arr:
            if is_ith_bit_set(num,idx):
                bucket1^=num
            else:
                bucket2^=num
        print(bucket1,bucket2)
        return bucket1,bucket2


sol = Solution()
arr1 = [1,2,1,2,3,3,4,5,5]
sol.singleI(arr1)

arr2 = [1,2,2,1,3,3,6,3,4,5,4,5,5,4,1,2]
sol.singleII(arr2)

arr3 = [1,1,2,2,3,3,4,4,5,5,6,6,9,12]
sol.singleIII(arr3)
