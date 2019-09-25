# We can combine for loops using nesting. 
# If we want to iterate over an (x,y) field
# we could use:


for x in range(1,10):
    for y in range(1,5):
        print("(" + str(x) + "," + str(y) + ")")