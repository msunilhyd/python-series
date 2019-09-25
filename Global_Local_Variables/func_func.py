# Calling functions inside functions


def highFive():
    return 5

def f(x,y):
    z = highFive()
    return x+y+z

print(f(3,2))


# If a variable can be reached anywhere in the code, it is called a global variable
# If a variable is known only inside a scope, we call it a local varible