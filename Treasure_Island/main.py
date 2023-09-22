def main():
    print('Welcome to the treasure island where you have to find the hidden treasure')

    var1 = input('You are at the infront of the island. You have to move straight: ')

    if var1.lower() == 'straight':
        print("You are walking in front, now there are 3 ways: straight, left, or right.")
        var2 = input('Which way would you like to go: ')

        if var2.lower() == 'straight':
            print('Your feet got stuck in quicksand, and you died.')
        elif var2.lower() == 'right':
            print('You got bit by a venomous snake and died because of poison.')
        elif var2.lower() == 'left':
            print('You find a cave with a cross marked inside, and you find the treasure!')
            print('Congratulations! You have found the hidden treasure and won the game.')

if __name__ == "__main__":
    main()
