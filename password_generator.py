import random
import string

def password_generator(pw_length):
    """
This program suggest password for you but it requires that you specify the length of the password you want
    
This program continues to run except you stop it. If you wish to quit enter 00
    """
    password = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return "".join(random.choice(password) for i in range(pw_length))
print(password_generator.__doc__)

while True:
    user= int(input('Enter your desired password length: '))
    if user == 00:
        break
    if user < 8:
        print('Your password length is weak, enter number greater than 8')
    else:  
        print(password_generator(user))