head=[1,2,3,4,6]
key=2

if head.next is None and head==key:
    return None

prev=None
temp=head
new_head=head

while temp is not None:
    if temp.val==key:
        if prev is not None:
            prev.next=temp.next
        if temp.next is not None:
            temp.next.prev=prev
        if temp==new_head:
            new_head=new_head.next
    prev=temp
    temp=temp.next
return new_head


# Time complexity=O(N), Space complexity=O(1)