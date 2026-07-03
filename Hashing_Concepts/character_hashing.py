s="azyxyyzaaaa"
q=["d","a","y","x"]

# hash_list=[0]*26
# for ch in s:
#     ascii_val=ord(ch)
#     index=ascii_val-97
#     hash_list[index]+=1
# for ch in q:
#     ascii_val=ord(ch)
#     index=ascii_val-97
#     print(hash_list[index])

# Time complexity=O(m+N), Space commplexity=O(26)≈O(1) 

hash_dict = {}
for ch in s:
    if ch in hash_dict:
        hash_dict[ch] += 1
    else:
        hash_dict[ch] = 1
for ch in q:
    if ch in hash_dict:
        print(hash_dict[ch])
    else:
        print(0)