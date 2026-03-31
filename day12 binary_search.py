arr=[10,20,30,40,50]
left=0
right=len(arr)-1
target=30
found=False
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        found=True
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
print(found)
