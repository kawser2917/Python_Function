'''
def arg_one(*args):
    for i in (args):
        print(i)

arg_one('kawser','kamrul','kaharul','shofiqul','kazoly')

'''

def arg_two(one,two,*args):
    print(one)
    print(two)
    for i in(args):
        print(i)
my_list=['Kawser','kamrul','kaharul']

arg_two(*my_list)
print()
arg_two("khairl",'khadem','kamrul','kaharul','kawser')

print()

arg_two("khairl",'khadem',*my_list)


