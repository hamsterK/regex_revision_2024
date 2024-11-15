import re

text = "0xf, 0xa, 0x5"
match = re.findall(r"0x[\da-fA-F]", text)
match2 = re.findall(r"[^0-9]", text)

print(match)
print(match2)


# . any symbol
# \d any digit
# \D any non-digit
# \s any space symbol
# \S any non-space symbol
# \w any word symbol [a-zA-Z0-9]
# \W non-word symbol
