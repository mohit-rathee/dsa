import heapq


class Solution:
    def min_no_of_platforms_opt(self, arrival, departure):
        trains = [(arrival[i], departure[i]) for i in range(len(arrival))]

        trains.sort(key=lambda x: x[0])

        platforms_dept = []
        count = 0

        for s, e in trains:
            if platforms_dept and s > platforms_dept[0]:
                heapq.heappop(platforms_dept)
            else:
                count += 1

            heapq.heappush(platforms_dept, e)

        print(platforms_dept)
        print(count)
        return count

    def min_no_of_platforms(self, arrival, departure):
        trains = [(arrival[i], departure[i]) for i in range(len(arrival))]
        trains.sort(key=lambda x: x[0])
        for t in trains:
            print(t)
        print()

        count = 0
        platforms_dept = []

        for train in trains:
            s, e = train
            # print(s, e)

            has_accomodated = False
            for idx in range(len(platforms_dept)):
                dept = platforms_dept[idx]

                if s > dept:
                    platforms_dept[idx] = e
                    has_accomodated = True
                    break
            if has_accomodated:
                continue
            else:
                count += 1
                platforms_dept.append(e)

        print()
        print(platforms_dept)
        print(count)
        return count


sol = Solution()
arrival = [900, 1100, 1235]
departure = [1000, 1200, 1240]
arrival = [900, 1000, 1200]
departure = [1000, 1200, 1240]
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
# arrival = [20, 30, 45]
# departure = [50, 40, 60]
sol.min_no_of_platforms(arrival, departure)
sol.min_no_of_platforms_opt(arrival, departure)
