def move_negatives(nums):
    negative = []
    positive = []

    for num in nums:
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)

    return negative + positive


nums = [1, -2, 3, -4, 5, -6]

print(move_negatives(nums))