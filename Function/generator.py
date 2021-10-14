# there i have create a generator function using yield 
def gen(a,b):
    yield a
    yield b

x,y=gen(10,20)
print(x)
print(y)
print()


print("your next function work like this ")

def gen2(x,y):
    yield x
    yield y
reult=gen2(1,2)
print(reult)
print(type(reult))

print(next(reult))
print(next(reult))

