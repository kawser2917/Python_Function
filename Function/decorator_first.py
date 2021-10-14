def upper_str(fucn):
    def inner():
        str1=fucn()
        return str1.upper()
    return inner

@upper_str

def print_msg():
    return 'good morning'

print(print_msg())