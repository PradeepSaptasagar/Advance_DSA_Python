head=[]

temp=head
while temp is not None:
    stack.append(temp.val)
    temp=temp.next
temp=head
while temp is not None:
    e=stack.pop()
    temp.val=e
    temp=temp.next
return head

# Time complexity=O(N), Space complexity=O(1)


if head.next is None:
    retrn head

curr=head
prev=None
while curr is not None:
    front=curr.next
    curr.next=prev
    curr.prev=front
    prev=curr
    curr=front
return prev

# Time complexity=O(N), Space complexity=O(1)
