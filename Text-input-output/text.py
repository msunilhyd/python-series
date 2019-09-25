# A string is a series of characters mostly used to display text.
# text between 2 quotes, Python accepts single, double and triple quotes.


s = "hello world"
print(s)

# To get text from keyboard

name = input("Enter your name : ")
print(name)


# String comparision
# To test if 2 strings are equal use the equality operator (==)
sentence = "The cat is brown"
q = 'cat'

if q == sentence:
    print('strings equal')
else:
    print('Hello Bhratha')


# To test if 2 strings are not equal use the inequality operator (!=)

sentence = "The city is small"
q = "king"

if sentence != q:
    print('sentences are not equal')
else:
    print('sentences are equal')


# String slicing str[0:3]

str = 'SunilMocharla'
print(str[0:2])
print(str[2:])