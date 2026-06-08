# hashmap approach
def two_sum_hashmap(nums, k):
    print(nums, k)
    hashmap = {}
    for idx, val in enumerate(nums):
        hashmap[val] = idx
    for num in hashmap:
        target = k - num
        if target in hashmap:
            return hashmap[num], hashmap[target]
    return -1, -1

# sort approach


def two_sum_sort(nums, k):
    sorted_nums = sorted(nums)
    i = 0
    j = len(sorted_nums)-1
    while j > i:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum > k:
            j -= 1
        elif sum < k:
            i += 1
        else:
            a, b = sorted_nums[i], sorted_nums[j]
            return nums.index(a), nums.index(b)


nums = [2, 6, 5, 8, 11]
k = 14
print(two_sum_hashmap(nums, k))
print(two_sum_sort(nums, k))
