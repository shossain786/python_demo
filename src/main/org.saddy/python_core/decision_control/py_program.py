 #! write a pyhton program for a company insures its drivers in the following cases: 
 #! - if the driver is married
 #! - if the driver is unmarried, male & above age 30
 #! - if the driver is unmarried, felame & above age 25
 #! in all other casses, the driver is not insured. 
 
married = input('Enter marital status: ')
gender = input('Enter you gender: ')
age = int(input('Enter you age: '))

if(married == 'm') or (married =='u' and gender == 'm' and age > 30) \
    or (married == 'u' and gender == 'f' and age > 25):
        print('Insured')
else:
    print('not insured')