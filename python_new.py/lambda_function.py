# a=lambda a,b:print(a+b)
# a(2,2)
#  # or
# a=lambda a,b:a+b
# print(a(2,3))

def fun(a):
    return lambda b:b*a
y=fun(10)
print(y(2))
