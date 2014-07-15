s = "a1 b5     t    t2        somestring1withnumber end"
import re 

p =  re.compile('[^\s]+')
m = p.match(s)
fa= p.findall(s)
srch= p.search(s)
print fa


