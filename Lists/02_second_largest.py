arr = [10, 5, 20, 8, 20, 15]

unique = list(set(arr))
unique.sort()

if len(unique) < 2:
    print("Second largest doesn't exist")
else:
    print(unique[-2])