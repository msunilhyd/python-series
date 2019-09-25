# Loops : For loop, while loop
# Code can be repeated using a loop

# Python has 3 types of loops, while loop, for loop and nested loop


# For loop
# We can iterate a list using a for loop

items = ["Abby", "Brenda", "Cindy", "Diddy"]

for item in items:
    print(item)

# The for loop can be used to repeat N times too:

for i in range(1, 10):
    print(i)


# If you are unsure of how many times a code should be repeated, 
# use a while loop

correct_number = 5
guess = 0

while guess!= correct_number:
    guess = int(input("Guess the correct number: "))

    if guess != correct_number:
        print('False guess')

print('You guessed the correct number')