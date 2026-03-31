arr=[1,1,2,2,2,3,3,4,4,5]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)