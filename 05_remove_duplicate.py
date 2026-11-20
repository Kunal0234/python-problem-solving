def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


nums = [1, 2, 2, 3, 4, 3, 5]

print(remove_duplicates(nums))