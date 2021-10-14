def upper_d(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner

def split_d(func):
    def inner():
        str2=func()
        return str2.split()
    return inner

@split_d #if we write this decorator instead of upper then we will get error because we are not able to use upper function in a list
@upper_d # This function will work first 
def message():
    return 'good morning'

print(message())
