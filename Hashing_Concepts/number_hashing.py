n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
    print(count)

# Time complexity=O(m X N), Space complexity=O(1)

hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])

# Time complexity=O(m + N), Space complexity=O(11)≈O(1)
freq_dict={}
for num in n:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1
for num in m:
    if num in freq_dict:
        print(freq_dict[num])
    else:
        print(0)

# Time complexity=O(m + N), Space complexity=O(k)