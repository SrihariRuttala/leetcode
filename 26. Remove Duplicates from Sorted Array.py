def removeDuplicates(nums):
    count=0
    for i in range(len(nums)):
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            continue
        nums[count] = nums[i]
        count+=1
    print(count)
    

arr = [int(i) for i in input().split()]
removeDuplicates(arr)