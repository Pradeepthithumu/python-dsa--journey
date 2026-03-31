arr=[1,2,3,4,5]
left=0
right=len(arr)-1
target=10
while left<right:
    current_value=arr[left]+arr[right]
    if current_value==target:
        print("pair:",arr[left],arr[right])
        break
    elif current_value<target:
        left+=1
    else:
        right-=1
print("no pair found")
