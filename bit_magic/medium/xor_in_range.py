class Solution:
    def xor_in_range(self, n):
        if n%4 == 0:
            return n
        if n%4 == 1:
            return 1
        if n%4 == 2:
            return n+1
        if n%4 == 3:
            return 0
        else: # just to soothe my lsp
            return 0
        
    def xor_in_given_range(self,start,finish):
        upto_start = self.xor_in_range(start-1)
        upto_finish=self.xor_in_range(finish)
        return upto_start^upto_finish


sol = Solution()
n = 4
print(sol.xor_in_range(n))
print(sol.xor_in_given_range(4,10))
