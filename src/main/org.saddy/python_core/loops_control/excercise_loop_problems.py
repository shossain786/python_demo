# Let Us Python: Page#86
#! g: What will be the output of the following code snippet?
for index in range(20, 10, -3):
    print(index, end=' ')
# Ans: Output:- 20 17 14 11
#!Understanding Range Function:
print()
for i in range(5):
    print(i, end=' ')
#Output: 0 1 2 3 4
print()
for i in range(1, 10, 3):
    print(i, end=' ')
#output = 1 4 7
print()
for i in range(1, 5):
    print(i, end=' ')
#Output: 1 2 3 4
print()
for i in range(-2):
    print(i, end=' ')
#Output: Nothing

#! D>a Write a program to print first 25 add numbers using range()
print('Program to print odd numbers using range')
for i in range(50):
    if i%2 != 0:
        print(i , end= ' ')
print()
print('End of the program')