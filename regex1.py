# REGEX

import re

print(re.search("hello","hello world hello world"))
if re.search("hello","hello world hello world"): print("YES")
print(re.findall("hello","hello world hello world"))
print(re.findall("car.","car care in tar with par"))

text=" car with care in cart in tar with part par"
print([i.span()[0] for i in re.finditer("car.",text)]) # starting-ending indexes

# span returns are tuple

print([ text[i.span()[0]:i.span()[1]] for i in re.finditer("car.",text)]) # span returns as tuple  dot (.) includes the space also

print([i for i in re.findall("[cp]ar.",text)]) # Case sensitive -> ['car ', 'care', 'cart', 'part'] NO par as it ends at 3 characters

print([i for i in re.findall("[a-cA-C]ar",text)])

print([i for i in re.findall("[^c]ar",text)]) # ['tar', 'par', 'par']

print(re.compile("[c]ar").sub("LOL",text)) # LOL with LOLe in LOLt in tar with part par
print(re.compile("[c]ar.").sub("LOL",text)) # LOLwith LOL in LOL in tar with part par

text = "hello \\and from .."

print(len(re.findall(r"\\and",text))) # raw string use r (Symbols)

text = "U.S.A A.S.A.P. G.B GR"

print(re.findall(".\..\..",text)) # ['U.S.A', 'A.S.A']

text = '''
this is
a multiline
text
'''
print(re.compile("multiline").sub("single line", (re.compile("\n").sub(" ",text)))) #  this is a single line text
