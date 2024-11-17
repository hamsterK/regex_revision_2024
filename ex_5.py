import re

text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b",text)
print(match)
print(match.group(1))
print(match.lastindex)
print(match.start(1))  # index of C in color... = 6
print(match.end(1))
print(match.end(2))
print(match.span(1))

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match.groupdict())
print(match.lastgroup)
print(match.expand(r"\g<key>:\g<value>"))  # \g<name> accessing group by name

"""
re.search - finds first match
re.finditer - finds all matches, iter obj
re.findall - list of all matches
"""
