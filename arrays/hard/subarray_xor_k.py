def count_subarray_xor_k(arr, k):
    print(arr)
    hashset = {}
    xor = 0
    sub_count = 0
    for num in arr:
        xor = xor ^ num
        if xor == k:
            sub_count += 1
        desired_xor = xor ^ k
        if desired_xor in hashset:
            sub_count += hashset[desired_xor]

        if xor in hashset:
            hashset[xor] = hashset[xor] + 1
        else:
            hashset[xor] = 1

    print(arr, k)
    print(sub_count)


arr = [4, 2, 2, 6, 4]
k = 6
# arr = [5, 6, 7, 8, 9]
# k = 5
count_subarray_xor_k(arr, k)
