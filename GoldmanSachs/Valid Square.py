# q2
from typing import List
from math import sqrt
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        hashmap={}
        self.distance(p1,p2,hashmap)
        self.distance(p1,p3,hashmap)
        self.distance(p1,p4,hashmap)
        self.distance(p2,p3,hashmap)
        self.distance(p2,p4,hashmap)
        self.distance(p3,p4,hashmap)
        # print(hashmap)
        if len(hashmap)==2:
                val=list(hashmap.values())
                val.sort()
                # print(val)
                keys=list(hashmap.keys())
                keys.sort()
                # print(keys)
                # print(sqrt(2)*keys[0])
                if int(keys[1])==int(sqrt(2)*keys[0]):
                    if val[0]==2 and val[1]==4:
                        return True
        return False
    def distance(self,a,b,h):
        d=sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))
        if d not in h :
            h[d]=1
        else:
            h[d]+=1
        return d

obj=Solution()
asn=(obj.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print(asn)