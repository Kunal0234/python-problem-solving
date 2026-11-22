def find_leaders(nums):
    leaders = []
    max_right = float('-inf')

    for num in reversed(nums):
        if num >= max_right:
            leaders.append(num)
            max_right = num

    return leaders[::-1]


nums = [16, 17, 4, 3, 5, 2]

print(find_leaders(nums))