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

def main():
    # alphabets, digits = count_alphabets_and_digits('Pune-411048')
    # print("Number of alphabets:", alphabets)
    # print("Number of digits:", digits)
    palindromeNumber()

if __name__ == "__main__":
    main()
