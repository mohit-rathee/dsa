import math


def koko_eating_banana(arr, goal):
    print(arr, goal)
    max_speed = max(arr)
    low,high = 1,max_speed
    while low<high:
        mid = (low+high)//2
        current_goal=0
        for banana in arr:
            # mid --> speed
            # time = distance/speed
            current_goal+= math.ceil(banana / mid)
            if current_goal>goal:
                break
        if(current_goal<=goal):
            # this speed works, now lets find a smaller one
            high = mid
        else:
            low= mid+1
    return low

arr = [7, 15, 6, 3]
goal = 8
# arr = [25, 12, 8, 14, 19]
# goal = 5
speed = koko_eating_banana(arr, goal)
print(speed)
