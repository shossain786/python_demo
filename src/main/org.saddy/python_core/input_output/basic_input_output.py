#! Basic practice of the Capter 7: Console Input/Output
#! Console Input
# the function input() returns a String type data. we can receive multiple values at a time
def basic_ip_op():
    s = input('Enter your name:')
    print(f'Your Name is: {s}')
    fname, lname = s.split()
    print(f'First Name: {fname} \nLast Name: {lname}')
#! Receive multiple int values and then convert them to ints
def mulitple_int_values():
    n1, n2, n3 = input('Enter three numbers: ').split()
    n1, n2, n3 = int(n1), int(n2), int(n3)
    print(n1*n1, n2*n2, n3*n3)
    
    #! similar to above we can optimize the code by following way!
    n1, n2, n3 = [int(n) for n in input('Enter three numbers: ' ).split()]
    print(n1*n1, n2*n2, n3*n3)
    
    #! multiple input with arbitrary number of values
    numbers = input('Enter the numbers: ').split()
    for n in numbers:
        print(n)
    
    #! input() can be used to received different types of values at a time
    data = input('Enter name, age, salary: ').split()
    name = data[0]
    age = data[1]
    salary = data[2]
    print(f'Name: {name}, \nAge: {age}, \nSalary: {salary}') 

def main():
    # basic_ip_op()
    mulitple_int_values()
    
if __name__ == "__main__":
    main()
    