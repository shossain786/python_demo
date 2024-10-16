 #! An f-string (Formatted String Literal) is a feature in Python that provides a more concise and readable way 
 #! ebmeded expressions inside string literal. F-String were intruduced in Python 3.6 and they allow you to insert
 #! variables expressions into string using curly {} braces.
 # Basic syntax: f'my text {expression}'  or  F'my text {expression}'
#! the f' or F' prefix before the string indicates that it's an f-string
#! Different Usecase
#! 1. Vvariable insertion
#! 2. Expression insertion
#! 3. Formatting numbers
#! 4: Calling function or methods

#Example 1:Variable insertion
name = 'Saddam'
age = 30
print(f'My name is {name}. I am of age {age}') # Example of variable insertion
# print('My name is {}. I am of age {}'.format(name, age)) #this is earlier approach/way to use

#Example 2: Expression insertion
num1 = 10
num2 = 30
print(F'Sum of the numbers {num1 + num2}')

#Example 3. Formatting numbers
pi = 3.14159
print(f'Two decimal pointer value of pi is {pi:.2f}')

#Exampe 4: Calling function or methods
name = 'saddam hossain'
print(f'My Name Is {name.title()}')
print(f'My Name Is {name.upper()}')
