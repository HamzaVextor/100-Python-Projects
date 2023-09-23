import sys

def easy_game():
    score = 0

    # Question 1
    print("Q1. What does HTML stand for")
    print('''
        a) Hyperlink Text Markup Language
        b) Hyper Text Makeup Language
        c) Hyper Text Markup Language
        d) High Tech Modern Language
    ''')
    
    q1_input = input("Please select an option: ")
    if q1_input == 'b':
        score += 100
        print(f'You got {score} points')
    elif q1_input != 'b':
        score -= 100
        print(score)
    else:
        print('wrong choice')

    # Question 2
    print("Q2. Which of the following is a front-end programming language?")
    print('''
        a) Java
        b) Python
        c) HTML
        d) PHP
    ''')
    
    q2_input = input("Please select an option: ")
    if q2_input == 'c':
        score += 100
        print(f'You got {score} points')
    elif q2_input != 'c':
        score -= 100
        print(score)
    else:
        print('wrong choice')

    # Question 3
    print('Q3. What does API stand for?')
    print('''
        a) Application Programming Interface
        b) Advanced Programming Interface
        c) Automated Process Integration
        d) Application Process Interface
    ''')
    
    q3_input = input("Please select an option: ")
    if q3_input == 'a':
        score += 100
        print(f'You got {score} points')
    elif q3_input != 'a':
        score -= 100
        print('You got', score)
    else:
        print('wrong choice')



def hard_game():
    score = 0

    # Question 1
    print("Q1. What is the time complexity of a binary search algorithm?")
    print('''
    a) O(1)
    b) O(log n)
    c) O(n)
    d) O(n^2)
    ''')
    
    q1_input = input("Please select an option: ")
    if q1_input == 'b':
        score += 100
        print(f'You got {score} points')
    elif q1_input != 'b':
        score -= 100
        print(score)
    else:
        print('wrong choice')

    # Question 2
    print("Q2. Which of the following design patterns is commonly used for database connection management?")
    print('''
        a) Singleton
        b) Factory
        c) Observer
        d) Adapter
    ''')
    
    q2_input = input("Please select an option: ")
    if q2_input == 'a':
        score += 100
        print(f'You got {score} points')
    elif q2_input != 'a':
        score -= 100
        print(score)
    else:
        print('wrong choice')

    # Question 3
    print('Q3. Which HTTP status code represents a successful response in a REST API?')
    print('''
a) 200 OK
b) 400 Bad Request
c) 404 Not Found
d) 500 Internal Server Error
    ''')
    
    q3_input = input("Please select an option: ")
    if q3_input == 'a':
        score += 100
        print(f'You got {score} points')
    elif q3_input != 'a':
        score -= 100
        print(score)
    else:
        print('wrong choice')


def main():
    print('Welcome to dev quiz game.')
    choice = input('Enter 1 for hard game and 0 easy game and 2 to exit: ')
    if choice == '1':
        hard_game()
    if choice == '0':
        easy_game
    if choice == '2':
        print('Thank you for playing')
        raise SystemExit
    
if __name__ == '__main__':
    main()
