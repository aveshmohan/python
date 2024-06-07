# def fun(*argus):
#     sum=0
#     for i in argus:
#         sum=sum+i
#     print(i)
# fun(10,20,30)


def fun(**argus):
    for i,j in argus.items():

       print(i,j)

fun(name='futura',age=2,palce='calicut')
