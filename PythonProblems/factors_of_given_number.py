num=36
result=[]
for i in range(1,num+1):
    if(num%i==0):
        result.append(i)
print(result)
# Time compexity=O(N), Space complexity=O(k)

result=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)
# Time compexity=O(N), Space complexity=O(k)

from math import sqrt
result=[]
for i in range(1,int(sqrt(num)+1)):
    if num%i==0:
        result.append(i)
        if num//i!=i:
            result.append(num//i)
    result.sort()
print(result)

# Time compexity=O(sqrt(N))+O(N log N), Space complexity=O(k)


