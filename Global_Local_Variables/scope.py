
# Variables can only reach the area in which they are defined, which is called scope
# By default, all variables declared in a function are local variables
# To access a global variable in side a function, its required to explicitly
# define 'global', change the type to global or add


def f(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print(' x * y = ' + str(x*y))
    z = 4
    print('z is : ' + str(z))
z = 3
f(3,2)