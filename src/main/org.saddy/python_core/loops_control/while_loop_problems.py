 #! Write a simple that receives 3 sets of values p, n, and r and calculate simple interest for each
# i = 1
# while i <= 3 :
#     p = float(input('Enter value p: '))
#     n = float(input('Enter value n: '))
#     r = float(input('Enter value r: '))
#     si = p * n * r/100
#     print('Simple interest i= Rs. ' + str(si))
#     i += 1

#! Problem 2
# Write a program that prints numbers from 1 to 10 using an infinite loop. All numbers should get printed in the same line
# i = 1
# while 1:
#     print(i, end=',', )
#     i += 1
#     if(i > 10):
#         break
# print()

#! Write a program that prints all unique combinations of 1,2 and 3
print('Execution Started')
i=1
while i <= 3:
    j = 1
    while j <=3:
        k = 1
        while k<=3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i += 1
    
for s in range(65, 70):
    print(chr(s), end=',')
print()
print(chr(80))
print('End of the program')