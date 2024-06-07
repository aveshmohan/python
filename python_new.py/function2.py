

def fun(a,b):
    print(a,b)
    b=a+b
    a=b-a
    b=b-a
    print(a,b)

a=int(input("enter a number"))
b=int(input("enter a number"))
fun(a,b)
