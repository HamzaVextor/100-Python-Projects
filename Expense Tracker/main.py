def expense():
    name_expense = input('What is the name of expense: ')
    price = int(input('What is the price: '))
    date = input('On what date you bought it: ')

    add_income = int(input('What is your in come: '))
    
    total = (add_income - price)
    
    print(f'The expense: {name_expense}, {price}, {date}')
    print(f'The total is: {total}')
    
expense()