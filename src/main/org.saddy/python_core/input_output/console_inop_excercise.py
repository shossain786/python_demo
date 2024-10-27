 #! Page no 97:
 #! question e.
def qn_e():
    name = 'Java'
    number = '9870987609'
    print(f'{name:10}:{number:10}')
    
#! page: 98
#!Question p

def qn_p():
    a = 12.34
    b = 234.34
    c = 444.34
    d = 1.23
    e = 34.67
    print(f'a = {a:>10}\nb = {b:>10}\nc = {c:>10}\nd = {d:>10}\ne = {e:>10}')   
#!Output
# a =      12.34
# b =     234.34
# c =     444.34
# d =       1.23
# e =      34.67

def main():
    # qn_e()
    qn_p()

if __name__ == '__main__':
    main()
    