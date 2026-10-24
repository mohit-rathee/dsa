class Solution:
    def standard_candy(self, ratings):
        print(ratings)
        n = len(ratings)
        if n == 0:
            return 0

        left = [1] * n
        right = [1] * n

        # Pass 1: Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Pass 2: Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # Combine both constraints
        candies = [max(left[i], right[i]) for i in range(n)]

        return sum(candies)

    def candy(self, ratings):
        print(ratings)
        if not len(ratings):
            return 0

        count = 1  # 1 candy to first candidate
        idx_of_last_max = 0
        left_child_candy = 1
        diff_btw_last_peak_and_its_successor = 0  # include last max

        for i in range(1, len(ratings)):
            child_rating = ratings[i]
            left_child_rating = ratings[i - 1]

            if left_child_rating < child_rating:
                # assign this kid 1 extra from last one
                child_candy = left_child_candy + 1
                # print("giving ", child_candy)
                count += child_candy
                left_child_candy = child_candy
                idx_of_last_max = i
            elif left_child_rating == child_rating:
                count += 1
                idx_of_last_max = i
                left_child_candy = 1
                diff_btw_last_peak_and_its_successor = 0
            else:
                child_candy = 1
                if left_child_candy == 1:
                    no_of_child_to_adjust = i - idx_of_last_max
                    if diff_btw_last_peak_and_its_successor > 1:
                        # exclude child at idx_of_last_max
                        no_of_child_to_adjust -= 1
                        count += 1 + no_of_child_to_adjust
                        diff_btw_last_peak_and_its_successor -= 1
                    else:
                        count += 1 + no_of_child_to_adjust

                else:  # when left child has more than 1 candy
                    # assign only 1 candy to this child
                    # print("giving 1")
                    diff_btw_last_peak_and_its_successor = (
                        left_child_candy - child_candy
                    )
                    count += child_candy

                left_child_candy = child_candy

        return count


sol = Solution()
ratings = [1, 0, 5]  # 5
ratings = [1, 2, 2]  # 4
ratings = [1, 2, 3]  # 6
ratings = [3, 2, 1]  # 6
ratings = [1, 3, 2, 1]  # 7
ratings = [1, 2, 5, 4, 3, 2, 1]  # 18
ratings = [1, 2, 5, 4, 5, 4, 3, 2, 1]  # 22
ratings = [2, 3, 2, 2, 1]  # 7
ratings = [3, 4, 3, 3, 2, 1]  # 10
ratings = [1, 2, 2]  # 4
ratings = [1, 2, 2, 1]  # 6
ratings = [1, 2, 3, 2, 2, 1]  # 10
# ratings = [0, 1, 0]  # 4

print(sol.candy(ratings))
print(sol.standard_candy(ratings))
