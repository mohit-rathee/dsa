from math import inf

from utils.matrix import printgrid


class Solution:
    def job_sequence_problem(self, jobs):
        print()

        # j[0] is id        1 <= N <= 104
        # j[1] is deadline  1 <= Deadline <= N
        # j[2] is profit    1 <= Profit <= 500

        # Profit is at max 3 digit
        # so job priority is deadline+profit/1000
        # to fill jobs from end we reverse the jobs
        # filling from start may result in filling
        # of less profitable jobs.
        # as jobs can be executed before deadline,
        # but not after it.

        jobs = sorted(jobs,
                      key=lambda j:j[1]+(j[2]/1000),
                      reverse=True
                      )

        printgrid(jobs)

        total_jobs=0
        profit=0
        idx=0
        max_time= max(jobs)[1]-1
        time = +inf
        # filling jobs from end
        while idx<len(jobs):
            job = jobs[idx]
            deadline = job[1]
            time = deadline - 1
            # selecting job to start at this time
            if idx>=len(jobs):
                break
            print('at time',time)
            if(time>=jobs[idx][1]):
                print('no job')
                continue
            #then execute it.(execution_time = 1)
            total_jobs+=1
            profit+=jobs[idx][2]
            print('run',jobs[idx])
            # skip jobs of this deadline
            curr_deadline = jobs[idx][1]
            while (idx<len(jobs) and
                   curr_deadline==jobs[idx][1]):
                print('skipping',jobs[idx])
                idx+=1


            # # job_idx+=1
        print(total_jobs,profit)
        return total_jobs,profit





sol = Solution()
# jobs=[ [1, 4, 20],[6,4,10],[5,4,100] , [2, 1, 10] , [3, 2, 400] , [4, 1, 30] ]
jobs=[ [1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15] ]
jobs = [ [1, 1, 100] , [2, 2, 200] , [3, 3, 300] , [4, 4, 400] ]
jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]
sol.job_sequence_problem(jobs)
