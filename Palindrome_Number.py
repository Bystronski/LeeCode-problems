def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = [i for i in str(x)]
    if x == x[::-1]:
        return True
    else:
        return False


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
