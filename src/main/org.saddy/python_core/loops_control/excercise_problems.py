#Page: 87
#! Write a program to count number of alphabets and number of digits in the String Pune-411048
def count_alphabets_and_digits(input_string):
    alphabet_count = 0
    digit_count = 0

    for char in input_string:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1

    return alphabet_count, digit_count

#! d: Enter 5 digit number through keyboard and reverse the number and check whether the number is palindrome or not.
def palindromeNumber():
    number = int(input('Enter a number:'))
    print('You have entered: ', number)
    original_num = number
    revised_num = 0
    while number > 0:
        revised_num  = 10*revised_num + number % 10 
        number = number // 10
    print('Revised Number: ', revised_num)
    if original_num == revised_num:
        print(original_num, 'is Palindrome')
    else:
        print(original_num, 'is not Palindrome')

#! e: Write a program to find the factorial value of any nubmer entered through the keyboard

def print_factorial():
    number = int(input('Enter a number: '))
    result = 1
    while number > 0 : 
        result  *= number
        number -= 1
    print('Factorial value is: ', result)

#! f: Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each 
#! digits is equal to the number itself. Then the number is called Armstrong numer.
#! For example: 153 is Armstrong number as 153  = (1*1*1) + (5*5*5) + (3*3*3)
def check_armstrong_number():
    final_number = 0
    i = 1
    for i in range(1,501):
        num = i
        while num > 0:
            reminder = num % 10
            final_number += reminder*reminder*reminder
            num //= 10
        
        if i == final_number:
            print("ArmStrong Number: ", i)
        i += 1
        final_number = 0

#! g: Write a program to print all prime numbers from 1 to 300 and print the number of prime numbers
def print_prime_numbers():
    count = 0
    for number in range(1, 301):
        prime = True
        divider = 2
        if number <= 2:
            continue
        
        while divider <= number // 2:
            if number % divider == 0:
                prime = False
                break
            divider += 1
            
        if prime == True:
            print(number, 'is Prime')
            count += 1
    
    print('Total number of prime is: ', count)
    print('End of the program.')
    
#! h: Write a program to print the multiplication number of the number entered by the user. The table should get displayed
#! in the following form:
#! 29 * 1 = 29
#! 29 * 2 = 58
#! ..
def print_multiplication_number():
    number = int(input('Enter a number: '))
    
    for i in range(1, 11):
        result = number * i
        print(F'{number} * {i} = {result}') #! F' is indicating formated String. We can use f' also

def main():
    # alphabets, digits = count_alphabets_and_digits('Pune-411048')
    # print("Number of alphabets:", alphabets)
    # print("Number of digits:", digits)
    # palindromeNumber()
    # print_factorial()
    # check_armstrong_number()
    # print_prime_numbers()
    print_multiplication_number()

if __name__ == "__main__":
    main()
