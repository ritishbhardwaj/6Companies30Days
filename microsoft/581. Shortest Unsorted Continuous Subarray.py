def sol(nums):
    l,r=0,len(nums)-1
    maxn,minn=0,len(nums)-1
    for i in range(len(nums)):   #left se right maxn chalao     and right se left minn chalao
        if nums[i]>nums[maxn]:
            maxn=i
        elif nums[maxn]>nums[i]:
            l=i
        if nums[len(nums)-i-1]<nums[minn]:
            minn=len(nums)-i-1

        elif nums[len(nums)-i-1]>nums[minn]:
            r=len(nums)-i-1
    if r>=l:
        return 0
    return l-r+1


nums = [1,3,2,2,2]
print(sol(nums))