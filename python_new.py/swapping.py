a=2
b=3
temp=a
a=b
b=temp
print(a,b)

a=4
b=5
b=a+b  # 9
a=b-a   #9-4=5
b=b-a    #9-5=4
print(f"result is {a},{b}")
