#! BUilt in function print() is used to send output to the screen.
#! print() function has below form 
# print(object, sep= ' ', end='\n', file=sys.stdout, flush=False)
# print('Md', 'Saddam', 'Hossain', sep='-', end='!')
# print()
# name = "Mohammad Saddam Hossain"
# for n in name.split():
#     print(f'{n:10}')

#! example of using format method: 
name, age, salary = 'Rahul', '30', '45000.00'
#! print in order by position of variable using empty{}
print('Name  = {}, Age = {}, Salary = {}'.format(name, age, salary))
#! print in any desired order
print('Age = {1}, Salary = {2}, Name = {0}'.format(name, age, salary))
#! print name in 15 columns, salary in 10 columns
print('Name = {0:20}, Salary = {1:10}'.format(name, salary))
print()

start, end, step =input('Enter start, end, step values: ').split()
for n in range(int(start), int(end), int(step)):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')

#left aligned printing
for n in range(int(start), int(end), int(step)):
    print('{0:<5}{1:<7}{2:<8}'.format(n, n**2, n**3))
    