class Solution:
    def lemonade_chnage(self, bills):
        cashbox={
                5:0,
                10:0,
                20:0,
                }

            
        def get_max_bill_for(amount):
            bills = sorted(cashbox.keys(),reverse=True)
            for bill in bills:
                if int(bill) <= amount and cashbox[bill]:
                    return bill
                    
        for bill in bills:
            cashbox[bill]=cashbox.get(bill,0)+1
            remaining = bill - 5
            while(remaining):
                max_bill = get_max_bill_for(remaining)
                if max_bill is None:
                    print('false')
                    return False
                remaining -= int(max_bill)
                cashbox[max_bill]-=1

        print('true')
        return True


sol = Solution()
bills = [5, 5, 10 ]
sol.lemonade_chnage(bills)
