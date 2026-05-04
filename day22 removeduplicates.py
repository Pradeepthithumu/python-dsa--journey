arr=[1,1,2,3,3,4,5]
j=0
for i in range(len(arr)):
    if arr[i]!=arr[j]:
        j=j+1
        arr[j]=arr[i]
print(arr[:j+1])