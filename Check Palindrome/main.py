def palindrome():
    enter_word = input('Enter a word: ')
    
    reverse_word = enter_word[::-1]
    
    if enter_word == reverse_word:
        print('Palindrome')
    else:
        print('Not palindrome')
        
palindrome()