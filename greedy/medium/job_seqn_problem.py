from utils.matrix import printgrid


class Solution:
    # j[0] is id        1 <= N <= 104
    # j[1] is deadline  1 <= Deadline <= N
    # j[2] is profit    1 <= Profit <= 500

    def job_sequence_problem_opt(self,jobs):
        if not jobs:
            return 0, 0

        jobs.sort(key=lambda job: job[2], reverse=True)

        n = len(jobs)
        max_deadline =  max(job[1] for job in jobs)
        max_slot = min(n,max_deadline)

        time = list(range(max_slot + 1))

        def find(slot):
            if time[slot] != slot:
                time[slot] = find(time[slot])
            return time[slot]

        total_jobs = 0
        total_profit = 0

        for job_id, deadline, profit in jobs:
            slot = find(min(deadline, max_slot))

            if slot == 0:
                continue

            total_jobs += 1
            total_profit += profit

            time[slot] = find(slot - 1)

        print(total_jobs,total_profit)
        return total_jobs, total_profit

    def job_sequence_problem(self, jobs):
        if not len(jobs): 
            return 0,0

        jobs = sorted(jobs,
                      key=lambda j:j[2],
                      reverse=True
                      )
        max_deadline_job = max(jobs,key=lambda j:j[1])
        max_deadline = max_deadline_job[1]

        # print(max_deadline)
        time = [0 for _ in range(min(max_deadline,len(jobs)))]
        # printgrid(jobs)

        total_jobs=0
        profit=0

        for job in jobs:
            deadline = job[1]
            # print(time)
            # print(min(deadline,len(time)-1))
            end = min(deadline-1,len(time)-1)
            unmarked=True
            for idx in range(end,-1,-1):
                if time[idx]==0:
                    time[idx]=1
                    total_jobs+=1
                    profit+=job[2]
                    unmarked=False
                    # print('job',job[0],'run')
                    # print(time)
                    break
            if end == len(time)-1 and unmarked:
                break



        print(total_jobs,profit)
        return total_jobs,profit





sol = Solution()
# jobs=[ [1, 4, 20],[6,4,10],[5,4,100] , [2, 1, 10] , [3, 2, 400] , [4, 1, 30] ]
# jobs=[ [1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15] ]
# jobs = [ [1, 1, 100] , [2, 2, 200] , [3, 3, 300] , [4, 4, 400] ]
# jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]
# jobs = [ [1,4,20], [2,1,10], [3,1,40], [4,1,30] ]
jobs = [
    [1, 1, 10],
    [2, 2, 20],
    [3, 3, 30],
    [4, 4, 40],
    [5, 5, 50]
]
sol.job_sequence_problem(jobs)
sol.job_sequence_problem_opt(jobs)
