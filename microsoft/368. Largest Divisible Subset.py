#    q5
'''Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

'''
check=[]
def sol(ind,arr,ds):
    stack=[]
    check=[]
    sub=[]
    n=len(arr)
    for i in range(n):
        for j in range(n):
            


nums = [1,2,3]
sol(0,nums,[])

'''
Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

========================================

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

'''