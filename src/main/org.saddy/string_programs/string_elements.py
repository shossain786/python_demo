msg = 'Saddam Hossain'
# print(msg[0])
# print(msg[4])
# print(msg[-0])
# print(msg[-1])
# print(msg[-6])

#! Sub-String can be sliced out of a string
print(msg[0:5])
print(msg[1:])
print(msg[:9])
print(msg[-3:])
print(msg[:-2])
# print(msg[20]) #it will throw:- IndexError: string index out of range
print('>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
#! String Properties. In Python String is immutable - they can not be changd
str = 'Pyhton'
# str[0] = 'O'
# print(str) #it results an error:- TypeError: 'str' object does not support item assignment
str = 'Python Programming '
print(str)
str = 'Welcome to ' + str
print(str)
# String can be replicated during printing
print(str * 10)