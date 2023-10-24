def lengthOfLastWord(s):
    split_list = s.split()
    if len(split_list) == 0:
        return 0
    last_word = split_list[-1]
    return len(last_word)


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("a"))
print(lengthOfLastWord("    day"))
