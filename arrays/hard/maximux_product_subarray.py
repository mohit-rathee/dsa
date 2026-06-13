def maxProductSubArray(arr):
    print(arr)
    # Store length of array
    n = len(arr)

    # Initialize prefix and suffix products
    pre, suff = 1, 1

    # Initialize answer as negative infinity
    ans = float("-inf")

    # Traverse from both front and back
    for i in range(n):
        # Reset prefix if zero
        if pre == 0:
            pre = 1

        # Reset suffix if zero
        if suff == 0:
            suff = 1

        # Multiply prefix with front element
        # print("pre ", pre, "into", arr[i], end=" => ")
        pre *= arr[i]
        # print(pre)

        # Multiply suffix with back element
        # print("suff ", suff, "into", arr[n - i - 1], end=" => ")
        suff *= arr[n - i - 1]
        # print(suff)

        # Update maximum product so far
        ans = max(ans, pre, suff)
    print(ans)

    # Return the result
    return ans


def maxProduct(nums):
    print(nums)
    res = nums[0]
    maxProd = nums[0]
    minProd = nums[0]

    # Traverse from second element
    for i in range(1, len(nums)):
        curr = nums[i]

        # print(curr)
        # Swap max and min if current is negative
        if curr < 0:
            maxProd, minProd = minProd, maxProd

        # Update max and min product
        # here we decide wheather i should be in subarray or not,
        # best product ending at i
        maxProd = max(curr, maxProd * curr)
        # worst product ending at i
        minProd = min(curr, minProd * curr)
        # print(maxProd, minProd)

        # Update result
        res = max(res, maxProd)

    print(res)
    return res


# arr = [1, 2, 3, 4, 5, 0]
# arr = [1, 2, -3, 0, -4, -5]
arr = [-1, -4, -6, 0, -4, -5]
maxProductSubArray(arr)
maxProduct(arr)
