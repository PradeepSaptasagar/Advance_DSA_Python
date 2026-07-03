n=1234
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
print(result)

if n==result:
    print(True)
else:
    print(False)
    
# Time complexity=O(log10(N)), Space complexity=O(1)