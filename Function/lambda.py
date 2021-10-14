print('Normal function')

def add(x,y):
    c=x+y
    print(c)
add(4,3)

print()

print("lambda function")

fun=lambda x: print(x)
fun(3)

print()

print("Additon subtruction multiplication and division in labda")

operation=lambda x,y: (x+y, x-y, x*y,x/y)
addition,sub,mul,div=operation(9,3)

print(addition)
print(sub)
print(mul)
print(div)
