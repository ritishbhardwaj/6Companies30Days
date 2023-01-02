def sol(hashmap,s):
    i=0
    j=i+3
    hashmap['a']=0
    hashmap['b']=0
    hashmap['c']=0
    count=0
    # while i<=len(s)-1-2 and j<=len(s)-1 :
    #     if 0 in hashmap.values():

    #     if 'a' in s[i:j] and 'b' in s[i:j] and 'c' in s[i:j]:
    for k,char in enumerate(s):
        # if 'a' in s[i:k+1]:
        #     hashmap['a']+=1
        # if 'b' in s[i:k+1]:
        #     hashmap['b']+=1
        # if 'c' in s[i:k+1]:
        #     hashmap['c']+=1
        # if k<3: continue
        for x in range(i,k):
            check=s[x:k+1]
            if 'a' in check and 'b' in check and 'c' in check:
                count+=1
    print(count)
        

hashmap={}
s = "aaacb"
sol(hashmap,s)
print(hashmap)
'''TLE has occured in this solution'''