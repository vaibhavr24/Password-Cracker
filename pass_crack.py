import string
from random import *

userpass = input('Enter your pass: ')
guess = ''

lowalphalist = list(string.ascii_lowercase)
uppralphalist = list(string.ascii_uppercase)
numbercount = [1,2,3,4,5,6,7,8,9,0]
passw = lowalphalist + uppralphalist + numbercount


while(guess!=userpass):
    guess = ''
    for ele in range(len(userpass)):
        guess_let = passw[randint(0,60)]
        guess = str(guess_let) + str(guess)

print('your password is: ',guess)
