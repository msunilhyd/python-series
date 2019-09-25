# There are two types of variables : global variables and local variables
# A global variable can be reached anywhere in the code, a local only in the scope



# Local variables x and y
def sum(x, y):
    sum = x + y
    return sum

print(sum(3,9))



z = 10

def afunction():
    global z
    z = 36
    print(z)


afunction()
print(z)