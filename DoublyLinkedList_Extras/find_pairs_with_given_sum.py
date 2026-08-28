temp=head
result={}
while temp1 is not None:
    temp2=temp1.next
    while temp2 is not None:
        if temp1.data+temp2.data==target:
            result.append([temp1.data,temp2.data])
        temp2=temp2.next
    temp1=temp1.next
return result

# Time complexity=O(N^2), Space complesity=O(1)


my_set=set()
temp=head
result=[]
while temp is not None:
    remaining=target-temp.data
    if remaining in my_set:
        result.append([remaining,temp.data])
    my_set.add(temp.data)
    temp=temp.next
return result

# Time complexity=O(N), Space complexity=O(N)


result=[]
left=head
right=head
while right.next is not None:
    right=right.next
    while left is not None and right is not None and left.data<right.data:
        total=left.data+right.data
        if total==target:
            result.append([left.data,right.data])
            left=left.data
            right=right.data
        elif total>target:
            right=right.prev
        else:
            left=left.next
return result

# Time complexity=O(N), Space complesity=O(1)
