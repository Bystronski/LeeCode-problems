def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    chars = []
    for m in s:
        if m == '(':
            chars.append(')')
        elif m == '[':
            chars.append(']')
        elif m == '{':
            chars.append('}')
        elif not chars or chars.pop() != m:
            return False
    return not chars


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("()[{}]"))
