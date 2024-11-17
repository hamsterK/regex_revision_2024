import re

text = "undergroundfloor fee under ground"
match = re.findall(r"\b(up|ground)\b", text)  # \b marks start/end of word
print(match)


# ^ start of text
# $ end of text
# \A start of text
# \b border of word
# \B border of non-word
# \Z end of text
# (?=exp) check for overlap
# (?!exp) check for non-overlap

text2= """<!DOCTYPE html>
<html>
<meta http-quiv="ContentType" content="text/html; charset=windows-1251">
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
<p align=center>Hello World!</p>
</html>
"""

match2 = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text2, re.MULTILINE)
print(match2)

match3 = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text2,  re.MULTILINE)
print(match3)

# (?(id|name)yes_patter)
# (?(id|name)yes_patter|no_patter)
match4 = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text2,  re.MULTILINE)
print(match4)

match5 = re.findall(r"""([-\w]+)  #select attribute
                    [ \t]*=[ \t]*  # then = and ""
                    (?P<q>[\"'])?  #check ""
                    (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))  # get attribute value
                    """,
                    text2, re.MULTILINE|re.VERBOSE)
print(match5)

"""
flags (?flags)
a = re.ASCII
i = re.INGORECASE
m = re.MULTILINE
s = re.DATALL . includes \n then
x = re.VERBOSE allows spaces and comments in regex
"""

text3 = "Python, python, PYTHON"
match6 = re.findall(r"(?im)python", text3)
print(match6)
