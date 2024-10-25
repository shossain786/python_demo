#! Basic practice of the Capter 7: Console Input/Output
#! Console Input
# the function input() returns a String type data. we can receive multiple values at a time
s = input('Enter your name:')
print(f'Your Name is: {s}')
fname, lname = s.split()
print(f'First Name: {fname} \nLast Name: {lname}')