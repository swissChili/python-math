import math

def get_all(num):
    nums = []
    i = 0
    # add all the numbers to a list
    while i < num:
        nums.append(i)
        i += 1
    # loop through list of nums
    for n, i in enumerate(nums):
        if i <= 1:
            pass
        else:
            iters = math.floor(num / i) - 1
            print(i, "iterations:", iters)
            for x in range(iters):
                index = n * x + i
                print(index)
                print("nullifying", nums[index])
                nums[index] = 0
    return nums

nums = get_all(23)
print(nums)
