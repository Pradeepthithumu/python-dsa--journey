x=[10,2,45,23,5]
maxval=x[0]
for num in x:
   if maxval<num:
        maxval=num
print(maxval)
print("------------------")
arr=[10,20,30,40]
print(arr[::-1])
print("------------------")
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
print("------------------")
arr=[10,20,30,40,50]
target=60
seen=False
for num in arr:
    if num==target:
        seen=True
print(seen)
print("------------------")

arr=[10,80,20,60,30,30,40,50,50]
unique=sorted(set(arr))
second_largest=unique[-2]
print(second_largest)