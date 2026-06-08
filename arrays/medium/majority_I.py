def majority_element(nums):
    element = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != element:
            count -= 1
            if count == 0:
                element = nums[i]
                count = 1
        else:
            count += 1
    return element


nums = [7, 0, 0, 0, 0, 7, 7, 7, 7]
print(majority_element(nums))
