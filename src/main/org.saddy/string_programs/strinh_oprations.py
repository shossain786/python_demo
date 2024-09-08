subj = 'Python'
print(subj * 15) #! it is printing the String 15 times
#! use of in
print('u' in subj) #! resule is False as u is not present in Python
print('o' in subj) #! resule is True as o is present in Python

#! use of some built in functions
# print(len(subj))
# print(min(subj)) #result (P): Character with minimum value(ASCII)
# print(max(subj)) #retuns (y): Character with maximum value(ASCII)

#!String methods
# print(type(subj)) #it prints the type of the variable
# print(id(subj)) #it prints the address ref of the variable
print('\n>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<\n')
#! use of random
# import random
# number = random.randint(100, 99999)
# print(number)
# # subj = subj.upper
# s = 'Hello'
# print(s.isalpha())
# print(s.startswith('He'))
# print(s.islower())
# print(s.endswith('llo'))
# print('\n>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<\n')
#! Search and replace
# course = 'Selenium Automation'
# print(course.find('nium'))
# print(course.replace('Selenium', 'API'))
# print('\n>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<\n')
#! Trims whitespace
# myName = ' Saddam Hossain '
# print(myName.lstrip()) #trims white space from left side
# print(myName.rstrip()) #trims white space from right side
# print(myName.strip())  #trims white space from both side
#! split and partition
# fav_book = "Java Programming"
# print(fav_book.split(' ')) #output:-['Java', 'Programming'] 
# print('_'.join(fav_book)) #output: J_a_v_a_ _P_r_o_g_r_a_m_m_i_n_g

#! String conversion
my_text = 'random string'
print(my_text.upper())      #output:- RANDOM STRING
print(my_text.capitalize()) #output:- Random string
print(my_text.title())      #output:- Random String
print(my_text.swapcase())   #output:- RANDOM STRING
#conversion string to int and vice-versa
s = '23'
a = 10
aa = str(a)
print(int(s))               #output:- 23
print(type(aa))             #output:- <class 'str'>
print(float('7.0987'))      #output:- 7.0987

#! String comparison
s1 = 'Python'
s2 = 'python'
s3 = 'Python'
s4 = 'Python 3'
print(s1==s2)               #output:- False
print(s1==s3)               #output:- True
print(s1==s4)               #output:- False
print(s1 <= s4)