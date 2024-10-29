#! Practice code for the usage of list in Python
#! Example of Lists:
nums = [10, 4, 44, 23, 3, 10]
names = ['Saddam', 'Ibrahim', 'Akram', 'Hasan']
print(nums)
print(names)
#! List can contain dissimilar type of data as well
myList = [10, 'Saddam', 120.23]
print(myList)
#! In list * can be used to repeat an element for n number of times
num = [10]*5
data = ['Hello'] * 10
print(num)
print(data)
#! Print can be done for a sliced
print(nums[2:5]) #! output: [44, 23, 3]
print(nums[1:])  #! output: [4, 44, 23, 3, 10]
print(nums[:4])  #! output: [10, 4, 44, 23]
print(names[8])  #! it will result:- IndexError: list index out of range