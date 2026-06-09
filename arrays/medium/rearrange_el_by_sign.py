def rearrange_el_by_sign(nums):
    result = [0 for i in range(len(nums))]
    postive_idx = 0
    negative_idx = 1
    for val in nums:
        if val >= 0:
            result[postive_idx] = val
            postive_idx += 2
        else:
            result[negative_idx] = val
            negative_idx += 2

    print(result)
    return result


nums = [1, 2, -4, -5]
nums = [1, 2, 3, -1, -2, -3]
nums = [1, 2, 3, -1, -2, -3]

rearrange_el_by_sign(nums)
