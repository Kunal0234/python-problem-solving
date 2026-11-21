def max_difference(nums):
    min_element = nums[0]
    max_diff = float('-inf')

    for num in nums[1:]:
        difference = num - min_element

        if difference > max_diff:
            max_diff = difference

        if num < min_element:
            min_element = num

    return max_diff


nums = [7, 1, 5, 3, 6, 4]

print(max_difference(nums))