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

text = 'Pune-411048'
alphabets, digits = count_alphabets_and_digits(text)
print("Number of alphabets:", alphabets)
print("Number of digits:", digits)