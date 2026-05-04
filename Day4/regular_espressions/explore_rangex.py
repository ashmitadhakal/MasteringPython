


import re

content = "as busy as bee"

#print(re.findall(r"b[a-z]+",content))

#r = re.compile(r"as")
#r=re.compile(r"b[a-z]+")
r=re.compile(r"[a-z]{2}")

#print(type(r))

#match the regular expression from the start of the content
#print(r.match(content))

#returns a list of the all matches
print(r.findall(content))

#returns all matches as match objects
#print(list(r.finditer(content)))


content = "red|green;blue:yellow"
r=re.compile(r"\||;|:")
print(r.split(content))
print(r.sub(",",content))

r = re.compile(r"[|;:]")
print(r.split(content))
print(r.sub(",",content))