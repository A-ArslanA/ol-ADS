def find_min_max(numbers):
    if not numbers: 
        return None, None

    min_val = max_val = numbers[0]

    for num in numbers:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val
