nums=[5,6,7,7,1,9,111,1,1,5,1,1]
x=1
freq_map={}
for i in range(1,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map)

# time complexity=O(N), space complexity=O(N)

hash_map={}
n=len(nums)
for i in range(1,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)

# time complexity=O(N), space complexity=O(N)