def outer(expr):
    def upper_d(func):
        def inner():
            str1=func()
            str2=str1.upper()
            return str2+ expr
        return inner
    return upper_d

@outer('Kawser')
def message():
    return 'good morning '

print(message())