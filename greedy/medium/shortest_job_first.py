class Solution:
    def sjf(self, bt):
        print(bt)
        bt.sort()
        wait=0
        time=0
        for burst_time in bt:
            wait+=time
            time+=burst_time
        ans = wait//len(bt)
        print(ans)
        return ans


sol = Solution()
bt=[4,1,3,7,2]
sol.sjf(bt)
