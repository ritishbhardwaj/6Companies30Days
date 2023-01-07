# 3.

from functools import lru_cache
class Solution:
    #======================Approach 1 ==================
    def trailingZeroes(self, n: int) -> int:

        @lru_cache
        def fact(n):
            if n==0:
                return 1
            if n==1:
                return 1
            if fact==2:
                return 2
            else:
                return n*fact(n-1)
        ans=fact(n)
        i=10
        count=0
        while True:
            if ans % i == 0:
                i*=10
                count+=1
            else:
                break
        return count

    #========================Approach 2===============
    def trailingZeroes2(self, n: int) -> int:
        res=0
        while True:
            if n<5:
                break
            else:
                n=n//5
                res+=n
        return res


obj=Solution()
n=4544
ans=obj.trailingZeroes(n)
print(ans)