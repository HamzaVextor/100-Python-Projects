import random

def random_pass():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%&*_0123456789"
    lenght_of_pass = int(input('Enter the lenght: '))
    password = ''
    
    for i in range(lenght_of_pass):
        password+=random.choice(chars)
    print(password)

random_pass()        