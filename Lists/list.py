# List is a sequence and a basic data structure. 
# A List may contain strings(text) and numbers.
# A List is similar to an array in other programming languages, 
# but has additional functionality



# We define lists with brackets[]. To access the data, these same
# brackets are used.


l = ["Drake", "Linus", "Rihanna", "Lincoln"]

print(l)
print(l[0])
print(l[1])


# Add and Remove

l = ["Drake", 'Linus', 'Lincoln']

print(l)
l.append('Victoria')
print(l)
l.remove("Drake")
print(len(l))


# Sort List
# We can use the sort() function to sort a List

l = ["Drake", "Derp", "Derek", "Dominique"]

print(l)
l.sort()
print(l)


# If you want to have the list in descending order, 
# use the reverse() function

l = ['Drake', 'Linus', 'Loop', 'Ranga', 'Mani']
print(l)
l.reverse()
print(l)