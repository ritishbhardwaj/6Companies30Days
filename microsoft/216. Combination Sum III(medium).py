
final=[]
def sol(ind,arr,size_combination,target,s,ds):
    if ind>=len(arr):
        if len(ds)==size_combination and target==0:
            final.append(list(ds))
            return
        return 
    
    if arr[ind]<=target:
        ds.append(arr[ind])
        sol(ind+1,arr,size_combination,target-arr[ind],s,ds)
        ds.remove(arr[ind])
    sol(ind+1,arr,size_combination,target,s,ds)
    
    
k = 7
n = 40
arr=[1,2,3,4,5,6,7,8,9]
summation=0
sol(0,arr,k,n,summation,[])
print(final)
