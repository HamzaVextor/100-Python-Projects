import sys

def print_question(questions, options):
    print(questions)
    for option in options:
        print(option)
    return input('Please select an option: ')

def display_score(score):
    print(f'The score is {score}')

def easy_game():
    score = 0

    questions = [
        {
            'question': 'Q1. What does HTML stand for?',
            'options': [
                "a) Hyperlink Text Markup Language",
                "b) Hyper Text Makeup Language",
                "c) Hyper Text Markup Language",
                "d) High Tech Modern Language",
            ],
            'correct_answer': 'b'
        },
        {
            "question": "Q2. Which of the following is a front-end programming language?",
            "options": [
                "a) Java",
                "b) Python",
                "c) HTML",
                "d) PHP",
            ],
            "correct_answer": "c",
        },
        {
            "question": "Q3. What does API stand for?",
            "options": [
                "a) Application Programming Interface",
                "b) Advanced Programming Interface",
                "c) Automated Process Integration",
                "d) Application Process Interface",
            ],
            "correct_answer": "a",
        },
    ]

    for question_data in questions:
        question = question_data['question']
        option = question_data['options']
        correct_answer = question_data['correct_answer']

        user_input = print_question(question, option)
        if user_input == correct_answer:
            score += 100
            display_score(score)
        else:
            score -= 100
            display_score(score)

def hard_game():
    score = 0

    questions = [
        {
            'question': 'Q1. What is the time complexity of a binary search algorithm?',
            'options': [
                "a) O(1)",
                "b) O(log n)",
                "c) O(n)",
                "d) O(n^2)",
            ],
            'correct_answer': 'b'
        },
        {
            "question": "Q2. Which of the following design patterns is commonly used for database connection management?",
            "options": [
                "a) Singleton",
                "b) Factory",
                "c) Observer",
                "d) Adapter",
            ],
            "correct_answer": "a",
        },
        {
            "question": "Q3. Which HTTP status code represents a successful response in a REST API?",
            "options": [
                "a) 200 OK",
                "b) 400 Bad Request",
                "c) 404 Not Found",
                "d) 500 Internal Server Error",
            ],
            "correct_answer": "a",
        },
    ]

    for question_data in questions:
        question = question_data['question']
        option = question_data['options']
        correct_answer = question_data['correct_answer']

        user_input = print_question(question, option)
        if user_input == correct_answer:
            score += 100
            display_score(score)
        else:
            score -= 100
            display_score(score)

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
