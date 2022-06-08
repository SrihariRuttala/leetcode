n = 2
nums = [1,3,6]

min = 0
max = len(nums) - 1
flag =0
while min<=max:
    mid = (min + max)//2
    if nums[mid] > n:
        max = mid-1
        print(max)
    elif nums[mid] < n:
        min = mid+1
    else:
        print(mid)
        flag =1
        break

if flag !=1:
    print(max+1)
