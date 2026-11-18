arr = [0, 1, 0, 3, 12]

non_zero = []

for num in arr:
    if num != 0:
        non_zero.append(num)

zeros = [0] * (len(arr) - len(non_zero))

result = non_zero + zeros

print(result)