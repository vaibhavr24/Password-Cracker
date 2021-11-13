import string
from random import *

userpass = input('Enter your pass: ')
guess = ''

lowalphalist = list(string.ascii_lowercase)
uppralphalist = list(string.ascii_uppercase)
passw = lowalphalist + uppralphalist


while(guess!=userpass):
    guess = ''
    for ele in range(len(userpass)):
        guess_let = passw[randint(0,51)]
        guess = str(guess_let) + str(guess)

print('your password is: ',guess)