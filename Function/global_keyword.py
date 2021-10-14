'''
a=50
def show():
    global a
    a=10
    print(a)
show()
print(a)
'''

#here we are using global keyword 
i=0
def show():
    global i
    i=i+1
    print(i)
show()
print(i)