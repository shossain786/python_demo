name = "Saddam Hossain" #basic declaration of Sting
print(name)

#if there are characters like '" or \ within a string, they can be retained in two ways:
# escape them by \
msg = 'he Said, \'Let Us dig into this.\''
print(msg)
# Prepend the string with a 'r' indicating that it is a raw string
msg = r'he Said, "Let Us dig into this."'
#! Mutiple line String can be 3 ways
#! 1. all but the last line ends with \
multiLine1 = 'He is a young boy, \
who is from West Bengal, \
and his age is 22'
print(multiLine1)

#! 2. Enclosed with """ or '''
multiLine2 = """He is a young boy,
who is from West Bengal,
and his age is 22
"""
print(multiLine2)
multiLine3 = '''He is a young boy,
who is from West Bengal,
and his age is 22
'''
print(multiLine3)

#! 3. Blindspot
multiLine4 = ('He is a brilliant guy. '
              'He is from a poor family.'
              )
print(multiLine4)