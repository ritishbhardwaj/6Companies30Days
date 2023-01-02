from math import gcd
def divide_all(num,numsDivide):
    for i in numsDivide:
        if i%num!=0:
            return False
    return True

def sol(nums,numsDivide):
        nums.sort()
        g=numsDivide[0]
        for x in numsDivide[1:]:
            g=gcd(g,x)
        
        for i ,x in enumerate(nums):
            if g%x==0:
                return i
        return -1   




 
nums = [2,3,2,4,3]
numsDivide = [9,6,9,3,15]
ans=sol(nums,numsDivide)
print(ans)