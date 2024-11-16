import re

text = "Google, Gooogle, Goooooooogle"
match = re.findall(r"o{2,5}", text)  # major mode - takes longest
match2 = re.findall(r"o{2,5}?", text)  # minor mode
match3 = re.findall(r"o{3,}", text)
match4 = re.findall(r"Go{,3}gle", text)

print(match)
print(match2)
print(match3)
print(match4)

phone = "89123456789"
match5 = re.findall(r"8\d{10}", phone)

print(match5)

"""
? = {0,1}
* = {0,}
+ = {1,}
"""
text3 = "aba, abba"
match6 = re.findall(r"abb?a", text3)

print(match6)
