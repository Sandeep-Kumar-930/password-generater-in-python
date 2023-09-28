import random
import string
password_length = int(input('Input the length of the password: '))

def makepassword (length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for i in range(length))

    return password
print('Your password is:' + makepassword(password_length))