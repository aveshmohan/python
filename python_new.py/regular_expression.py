#methods
import re

# txt='the rain in spain'
# a=re.search('in',txt)
# print(a)

# txt='the rain in spain'
# a=re.findall('in',txt )
# print(a)

# txt='the rain in spain'
# a=re.split(" " ,txt)
# print(a)

# txt='the rain in spain'
# a=re.sub("", sub,txt)
# print(a)

txt='the rain in spain'
x=re.search('in',txt)
print(x)
print(x.span())
print(x.string)
print(x.group())

