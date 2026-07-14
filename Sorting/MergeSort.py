nums=[] # contains n number of elements
def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(i),len(j)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2           
    left_arr=nums[:mid]
    right_arr=nums[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)