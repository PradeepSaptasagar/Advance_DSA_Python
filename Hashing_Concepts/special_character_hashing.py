s = "a!y@y!a"
q = ["!", "@", "x"]

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

hash_list = [0] * 128 

for ch in s:
    index = ord(ch)  # Use the absolute ASCII value directly as the index
    hash_list[index] += 1

for ch in q:
    index = ord(ch)
    print(hash_list[index])