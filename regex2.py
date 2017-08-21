text = "hello \\and from .."

print(len(re.findall(r"\\and",text))) # raw string use r (Symbols)

text = "U.S.A A.S.A.P. G.B GR"

print(re.findall(".\..\..",text)) # ['U.S.A', 'A.S.A']

text = '''
this is 1111
a multiline
text 3
'''
print(re.compile("multiline").sub("single line", (re.compile("\n").sub(" ",text)))) #  this is a single line text


# \b : backspace, \f form feed, \t tab, \v vertical tab \r carriage return

print(len(re.findall("\d",text))) #[0-9] D-> [^0-9]

print([x for x in (re.findall("\d{2}",text))]) # \d{2} -> 2 digits ['11', '11']


mynums="1 12 123 1234 12345 123456 12345678910"
print((re.findall('\d{3,5}',mynums))) #between 3 and 5 digits -> ['123', '1234', '12345', '12345', '12345', '67891']
tel="416-828-5148"
if re.search("\w{3}-\w{3}-\w{4}","123-123-1234"): print("ok!") #

if re.search("\w{2,20}","st"): print("between 2 and 20") # between 2 and 20

# \s for space \S -> ^s

if re.search("\w{2,10}\s\w{2,10}","stelios stel"): print("between 2 and 10 then space then between 2 and 10") #between 2 and 10 then space then between 2 and 10

print(len(re.findall("s+","stelios scope soup trim"))) # found 4 [s,s,s]

if re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}","stelios@sot.com"): print("valid email")

