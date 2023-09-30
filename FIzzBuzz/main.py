def fizzbuzz(n):
    if n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    elif n % 3 and n % 5 == 0:
        print('fizzbuzz')
        
n = 27

fizzbuzz(n)