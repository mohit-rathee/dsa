# dutch national flag algorithm
def sort_0_1_2(arr):
    i = 0  # zero pointer
    j = len(arr)-1  # two pointer
    idx = 0
    while idx < j:
        val = arr[idx]
        if val == 0:
            # swap el to zero pointer
            arr[i], arr[idx] = arr[idx], arr[i]
            print('swap in ', i, idx)
            i += 1
            idx += 1
        elif val == 2:
            arr[j], arr[idx] = arr[idx], arr[j]
            print('swap in ', j, idx)
            j -= 1
        else:
            idx += 1
        print(arr)


arr = [1, 0, 2, 1, 0]
print(arr)
sort_0_1_2(arr)
print(arr)
