import re

print('Enter password')
password = input()
passReg1 = re.compile('[a-zA-Z0-9._%+-]{8,}') # least eight characters long
passReg2 = re.compile("[a-z]+[A-Z]") # contains both uppercase and lowercase characters
passReg3 = re.compile("[0-9]") # has at least one digit

def detect(text):
    if passReg1.search(text) == None:
        print('not strong')
    elif passReg2.search(text) == None:
        print('not strong')
    elif passReg3.search(text) == None:
        print('not strong')
    else:
        print('password is strong')

detect(password)