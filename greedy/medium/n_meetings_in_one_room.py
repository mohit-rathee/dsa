class Solution:
    def n_meetings_in_one_room(self, start,end):
        print(start)
        print(end)

        for i in range(len(start)):
            s = start[i]
            e = end[i]
            end[i] = (s,e,i)

        print()
        end.sort(key=lambda g:g[1])
        for i in end:
            print(i)

        order = []
        count = 0
        last_meeting_end = 0
        for meeting in end:
            s,e,i = meeting
            if s > last_meeting_end:
                # place meeting
                order.append(i)
                count+=1
                last_meeting_end = e
        print(count,order)

        # if i start filling short meetings first 
        # between slots. And check later if any
        # meeting is cancelling more meetings
        # then accomodate that one.

sol = Solution()
start = [1, 3, 0, 5, 8, 5] 
end = [2, 4, 6, 7, 9, 9]
sol.n_meetings_in_one_room(start,end)
