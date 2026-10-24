class Solution:
    def extend(self, arr, start, end):
        for i in range(start, end):
            arr[i] += 1

    def candy(self, ratings):
        print(ratings)
        if not len(ratings):
            return 0

        count = 1  # 1 candy to first candidate
        idx_of_last_max = 0
        left_child_candy = 1
        gap = 0  # include last max
        # candy_arr = [0 for _ in range(len(ratings))]
        # candy_arr[0] = 1

        # print(0, ratings[0], "giving 1")
        # print(candy_arr)

        for i in range(1, len(ratings)):
            child_rating = ratings[i]
            left_child_rating = ratings[i - 1]
            # print(i, ratings[i], end=" ")

            if left_child_rating < child_rating:
                # assign this kid 1 extra from last one
                child_candy = left_child_candy + 1
                # candy_arr[i] = child_candy
                # print("giving ", child_candy)
                count += child_candy
                left_child_candy = child_candy
                idx_of_last_max = i
            elif left_child_rating == child_rating:
                count += 1
                idx_of_last_max = i
                left_child_candy = 1
                gap = 0
                # candy_arr[i] = 1
            else:
                if left_child_candy == 1:
                    if gap > 1:
                        no_of_child_to_inc = i - idx_of_last_max - 1
                        # self.extend(candy_arr, idx_of_last_max + 1, i)
                        # candy_arr[i] = 1
                        # print(count_of_childs_in_between)
                        count += 1 + no_of_child_to_inc
                        # print(
                        #     "g>1",
                        #     "giving 1 +",
                        #     no_of_child_to_inc,
                        #     "for",
                        #     no_of_child_to_inc,
                        #     "childs",
                        # )
                        gap -= 1
                    else:
                        no_of_child_to_inc = i - idx_of_last_max
                        # self.extend(candy_arr, idx_of_last_max, i)
                        # candy_arr[i] = 1
                        count += 1 + no_of_child_to_inc
                        # print(
                        #     "g=1",
                        #     "giving 1 +",
                        #     no_of_child_to_inc,
                        #     "for",
                        #     no_of_child_to_inc,
                        #     "childs",
                        # )

                else:  # when left child has more than 1 candy
                    # assign only 1 candy to this child
                    # print("giving 1")
                    # candy_arr[i] = 1
                    gap = left_child_candy - 1
                    # print("gap", gap)
                    count += 1
                left_child_candy = 1
            # print(candy_arr)

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

print(sol.candy(ratings))
