def find_repeating_and_missing_num1(arr):
    s1 = 0
    s2 = 0
    for num in arr:
        s1 += num
        s2 += num * num

    N = len(arr)
    S1 = (N * (N + 1)) // 2
    S2 = (N * (N + 1) * (2 * N + 1)) // 6
    # X is missing
    # Y is repeating

    # X-Y = S1 - s1                     (1)
    X_mius_Y = S1 - s1

    # X^2 - Y^2 = S2 - s2 => (X+Y)(X-Y) (2)
    # (2)/(1) => X+Y                    (3)
    X_plus_Y = (S2 - s2) // (S1 - s1)

    # (3)+(1) => X = (X_plus_Y+X_mius_Y)//2
    X = (X_plus_Y + X_mius_Y) // 2

    # (3)-(1) => Y = (X_plus_Y-X_mius_Y)//2
    Y = (X_plus_Y - X_mius_Y) // 2
    print(Y, X)


def find_repeating_and_missing_num2(arr):
    xor = 0

    # XOR of elements and first N natural numbers
    for i in range(len(arr)):
        xor = xor ^ arr[i]
        xor = xor ^ (i + 1)

    # Get the rightmost set bit in xor
    number = xor & ~(xor - 1)

    # Group the numbers based on the differentiating bit
    # Number that falls into the 0 group
    zero = 0

    # Number that falls into the 1 group
    one = 0

    for i in range(len(arr)):
        """ Check if nums[i] belongs to the 1 group
         based on the differentiating bit"""
        if (arr[i] & number) != 0:
            one = one ^ arr[i]

        else:
            zero = zero ^ arr[i]

    for i in range(1, len(arr) + 1):
        if (i & number) != 0:
            one = one ^ i

        else:
            zero = zero ^ i

    cnt = 0

    for i in range(len(arr)):
        if arr[i] == zero:
            cnt += 1

    if cnt == 2:
        """ zero is the repeating number,
         one is the missing number"""
        print(zero, one)
        return [zero, one]

    """ one is the repeating number, 
    zero is the missing number"""
    print(one, zero)
    return [one, zero]


arr = [1, 2, 4, 4, 5, 6, 7, 8, 10, 9]
print(arr)

find_repeating_and_missing_num1(arr)
find_repeating_and_missing_num2(arr)
