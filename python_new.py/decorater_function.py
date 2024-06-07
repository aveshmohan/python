def my_decorator(fun):
    def demo():
        print("something is happening before the function is called")
        fun()
        print("something is happening after function is called")
    return demo

@my_decorator
def function1():
    print("hello")

function1()
