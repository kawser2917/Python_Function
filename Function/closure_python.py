'''
There outer function will execute first then it will see there have variable 3.so it will keep x=3
and then this will go to inner funcion call and this will see there have a parameter which argument is 
3 after that it will perform the arithmetic operation.

NOTE: we can not call inner function outside it's scope area. That's why we need closure

def outer():
    x=3
    def inner(y):
        print(x+y)
    inner(3)
outer()

'''
'''Closure
NOTE: By using closure we can easily user inner function outside it's scope
'''
def outer():
    x=3
    def inner(y):
        print(x+y)
    return inner
a=outer()
print(a(3))

