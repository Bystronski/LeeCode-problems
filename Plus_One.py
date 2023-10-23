def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    for i, d in reversed(list(enumerate(digits))):
        if d < 9:
            digits[i] += 1
            return digits
        elif d == 9:
            digits[i] = 0
    return [1] + digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
