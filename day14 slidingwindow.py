arr = [1, 3, 2, 6, 4, 1]
k = 2

window_sum = sum(arr[:k])   
max_sum = window_sum

for i in range(k, len(arr)):
    
    window_sum = window_sum + arr[i] - arr[i - k]

    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum Sum:", max_sum)