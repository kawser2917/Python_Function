def div_deco(func):
    def inner(x,y):
        if y==0:
            return 'Input valid value'
        return func(x,y)
    return inner

@div_deco
def div(a,b):
    return a/b
print(div(10,3))
        