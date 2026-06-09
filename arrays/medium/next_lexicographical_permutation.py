# reverse func
def reverse(arr, start=0, end=None):
    length = len(arr)
    if end is None:
        end = length - 1
    length = end - start + 1
    if (start == end):
        return
    for i in range(start, start+length//2):
        opp_idx = end - i + start
        temp = arr[opp_idx]
        arr[opp_idx] = arr[i]
        arr[i] = temp


def next_lexicographical_permutation(nums):
    print(nums)
    pain_point = -1
    for i in range(len(nums)-2, -1, -1):
        if (nums[i] < nums[i+1]):
            print(nums[i])
            pain_point = i
            break
    if pain_point == -1:
        return list(reversed(nums))
    relief_point = -1
    for i in range(len(nums)-1, pain_point, -1):
        if (nums[i] > nums[pain_point]):
            print(nums[i])
            relief_point = i
            break
    nums[pain_point], nums[relief_point] = nums[relief_point], nums[pain_point]
    reverse(nums, pain_point+1, len(nums)-1)
    return nums


nums = [3, 2, 1]
nums = [1, 2, 3, 6, 5, 4]
print(next_lexicographical_permutation(nums))
