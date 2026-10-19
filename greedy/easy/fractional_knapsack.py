class Solution:
    def frac_knapsack(self, val,wi,cap):
        n = len(val)
        worth_ratio = [val[i]/wt[i] for i in range(n)]
        sorted_worth_ratio = sorted(enumerate(worth_ratio),key=lambda r:r[1],reverse=True)
        total_value = 0
        for idx,_ in sorted_worth_ratio:
            value, weight = val[idx],wt[idx]
            if cap >= weight:
                cap-= weight
                total_value+=value
                # print('fully added',value,weight)
            else:
                portion = cap/weight
                # print('for',value,weight,portion,'%',round(value*portion,6))
                total_value+=round(value*portion,6)
                break
        # print(total_value)
        return total_value
                

sol = Solution()
val = [100,60]
wt = [30,30]
val = [100,100,100,100]
wt = [40,10,30,20]
capacity = 50
sol.frac_knapsack(val,wt,capacity)
