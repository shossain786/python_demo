 #! Q1. I have a text SaddamHossain. Help me to write a code in python in order to print in like [Saddam][Hossain]
 
import re
def print_text_with_braces():
    text = input('Enter Text: ')
    parts = re.findall(r'[A-Z][a-z]*', text)
    print(parts)
    formatted_text = ''.join([f'[{part}]' for part in parts])
    print(formatted_text)
         
def main():
    print_text_with_braces()
    
    
if __name__ == "__main__":
    main()