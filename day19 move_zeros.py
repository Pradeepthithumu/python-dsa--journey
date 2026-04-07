arr=[0,2,4,0,5,3]
n=len(arr)
j=0
for i in range(n):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j] 
        j+=1
print(arr)