#==================TLE (naive)======================
def sol(arr):
    g=[[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            g[j][i]=arr[i-j]
    print(g)
    # F=[0 for _ in range(len(g))]
    F=[0]*len(g)
    print(F)
    for i,gg in enumerate(g):
        sum=0
        f=0
        for j,ggg in enumerate(gg):
            f+=(j*ggg)
        F[i]=f
    print(max(F))


nums = [4,3,2,6]
sol(nums)



def sol1(arr):
    s=sum(arr)
    base=[i*arr[i] for i in range(len(arr))]
    n=len(arr)
    res=sum(base)
    f=sum(base)
    for i in range(n-1,-1,-1):
        f=f+s-(n*arr[i])
        res=max(f,res)
    print(res)


arr=[4,3,2,6]
sol1(arr)
