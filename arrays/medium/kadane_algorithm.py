def kadane_algorithm(nums):
    final_s = final_e = 0
    s = 0
    max_sum = float('-inf')
    sum = 0
    for idx, val in enumerate(nums):
        sum += val
        if max_sum < sum:
            max_sum = sum
            final_e = idx

        else:
            if sum <= 0:
                s = idx
                sum = 0
        print(val, '|', sum, max_sum)
        print(s, idx, '|', final_s, final_e)
    return max_sum


nums = [2, 3, -6, -2, 7, -4]
print(kadane_algorithm(nums))
