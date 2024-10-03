#  Wrtie a program discount is 10% offered is purchsed amount is more than 1000. Write a program to calculate the 
#  total expanses
qty = int(input('Enter purchased quantity: '))
price = float(input('Enter the price: '))
if qty > 1000:
    dis = 10
else:
    dis = 0
totalexp = qty * price - qty * price * dis/100
print('Total expense: Rs. ' + str(totalexp))