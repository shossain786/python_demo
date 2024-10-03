print(10<20)                #! yields True
print('Santosh' < 'Adi')    #! yields False
a = 10
b = 12
c = 14
print(a<b<c)                #! yeilds True
print(10 != 20 != 10)       #! yeilds True

#! Rule: Any non zero number(positive/negative/decimal) returns True and zero returns False
print(bool(10))             #! yeilds True
print(bool(-23))            #! yeilds True
print(bool(29.34))          #! yeilds True
print(bool(0))              #! yeilds False
print('------------------------------------Logical Operators-----------------------------------')
# And operator evaluates ALL expressions. it returns last expression if all expressions evaluates to Ture. 
# Otherwis, it returns first value that evaluates to False
a=30
b=27
x = 45 and a>20 and b < 50 and 38