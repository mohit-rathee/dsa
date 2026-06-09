def subarraySum(arr, k):
    # Size of the array
    n = len(arr)

    # Dictionary to store frequency of prefix sums
    prefixSumCount = {}

    # Initialize prefix sum and count of subarrays
    prefixSum = 0
    count = 0

    # Base case: prefix sum 0 has occurred once
    prefixSumCount[0] = 1

    # Traverse through the array
    for i in range(n):
        # Add current element to prefix sum
        prefixSum += arr[i]

        # Calculate the prefix sum that needs to be removed
        remove = prefixSum - k

        # If this prefix sum has been seen before,
        # add its count to the result
        if remove in prefixSumCount:
            count += prefixSumCount[remove]

        # Update the frequency of the current prefix sum
        prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1

    # Return the total count of subarrays
    return count


arr = [3, 1, 2, 4]
k = 6

print(subarraySum(arr, k))
