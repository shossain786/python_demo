 #! Problem 1
a = int(input('Enter value of a: '))
if(a<10):
    b = 20
else:
    b = 30

print(b)

#  ! problem 2
time = int(input('Enter the time: '))
if(time<12):
    print('Morning')
else:
    print('Afternoon')
    
# ! problem 3. Print following program in one line approach.
# x = 3
# y = 4.0
# if x == y:
    # print('x and y are equal')
# else:
    # print('x and y are not equal')

#! Solution
x = 3
y = 4.0

print('x and y are equal') if(a == b) else print('x and y are not equal')