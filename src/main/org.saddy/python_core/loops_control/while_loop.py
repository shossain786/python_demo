 #! Repetition Control Instruction with While Loop
#!Example1
# num = int(input('Enter a number: '))
# while num != 10:
#     print(num, num*num)
#     num = int(input('Enter a number: '))

#!Example2
# count = 0
# while count < 10:
#     print(count, count*count, count*count*count)
#     count +=1
#!Example3
s='Selenium'
lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
tpl = (10, 15, 25, 30, -20, -10)
i=0
while i < len(lst):
    print(i, s[i], lst[i], tpl[i])
    i += 1
print('Execution Completed')