from utils.matrix import printgrid


class Solution:
    def job_sequence_problem(self, jobs):
        print()

        # j[0] is id        1 <= N <= 104
        # j[1] is deadline  1 <= Deadline <= N
        # j[2] is profit    1 <= Profit <= 500

        # Profit is at max 3 digit
        # so job priority is deadline*profit/1000
        # to get things reversed in group
        # we'll use deadline*(1-profit/1000)

        jobs = sorted(jobs,
                      key=lambda j:j[1]*(1-j[2]/1000)
                      )

        printgrid(jobs)

        total_jobs=0
        profit=0
        time= 0
        for job in jobs:
            if time<job[1]: # in deadline
                #then execute it.(execution_time = 1)
                time+=1
                total_jobs+=1
                profit+=job[2]
                print('executing ',job)
        print(total_jobs,profit)
        return total_jobs,profit





sol = Solution()
# jobs=[ 
#       [1, 4, 20] ,
#       [2, 1, 10] ,
#       [3, 1, 40] ,
#       [4, 1, 30] 
#       ]
jobs=[ [1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15] ]
sol.job_sequence_problem(jobs)
