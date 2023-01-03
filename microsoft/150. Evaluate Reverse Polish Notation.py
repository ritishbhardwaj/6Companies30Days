#   q1
import math
def sol(arr):
    stack=[]
    operands=["+", "-", "*","/"]
    for i in range(len(arr)):
        if arr[i] not in operands:
            stack.append(int(arr[i]))
        else:
            x=stack.pop()
            y=stack.pop()
            if arr[i]=='+':
                stack.append(y+x)
            elif arr[i]=='-':
                stack.append(y-x)
            elif arr[i]=='*':
                stack.append(x*y)
            else:
                # p=math.floor(y/x) if y/x > 0 else math.ceil(y/x)
                p=y/x
                stack.append(math.trunc(p))
    print(stack)

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol(tokens)
# math.trunc()




'''Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''