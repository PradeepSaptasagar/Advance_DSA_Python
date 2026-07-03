n=5438
num=n
count=0
while(num>0):
    count+=1
    num=num//10
print(count)

# 2nd approach using logarithmic 
from math import *
def countDigits(num):
    return int(log10(num)+1)
print(countDigits(num))

# Time complexity = O(log10(N)), Space complexity=O(1) for both