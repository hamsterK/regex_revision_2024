import re

text = "+7(123)456-78-90"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)  # match from very beginning of string
print(m)

text2 = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8482" lat="52.6274" />; <point lon="41.8482" lat="53.6274" />
<point lon="424.8482" lat="54.6274" />, <point lon="43.8482" lat="55.6274" />
"""
m2 = re.split(r"[\n;,]+", text2)
print(m2)

text3 = """Moscow
Minsk
Warsaw
Vilnius
"""
count = 0


def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"


# m3 = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text3)  # substitute
m3 = re.sub(r"\s*(\w+)\s*", replFind, text3)  # substitute
print(m3)

m4, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text3)  # sub + number of subs
print(m4, total)

print("*****************")
rx = re.compile(r"\s*(\w+)\s*")  # complie regex to re-use it several times as rx
m5, total2 = rx.subn(r"<option>\1</option>\n", text3)
m6 = rx.sub(replFind, text3)
print(m5, total2, m6, sep="\n")
