def add(a, b):
    return float(a) + float(b)

def Subtract(a, b):
    return float(a) - float(b)

def division(a, b):
    if b==0:
        return "Cannot divide by 0"
    return float(a) / float(b)

def multiplication(a, b):
    return float(a) * float(b)

def main():
    while True:
        print('\n')
        print('What would you like to choose')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Division')
        print('4. Multiplication')
        print('5. Exit')

        choice = input("Select options from 1/2/3/4/5: ")
        if choice == '5':
            break
        
        print('\n')

        a = input('Enter Num: ')
        b = input('Enter Num: ')

        if choice == '1':
            print(f'{a} + {b} = {add(a, b)}')
        if choice == '2':
            print(f'{a} - {b} = {Subtract(a, b)}')
        if choice == '3':
            print(f'{a} / {b} = {division(a, b)}')
        if choice == '4':
            print(f'{a} x {b} = {multiplication(a, b)}')




if __name__ == "__main__":
    main()
