import random

def main():
  swg = input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: ")
  options = ["Rock", "Paper", "Scissors"]
  if swg == '0':
    user_choice = "Rock"
  if swg == '1':
    user_choice = "Paper"
  if swg == '2':
    user_choice = "Scissors" 

    print(user_choice)

  com = random.choice(options)
  print(com)

if(user_choice == 'Rock' and com == 'Paper') or (user_choice == 'Paper' and com == 'Scissores') or (user_choice == 'Scissors' and com == 'Rock'):
      print("User won")
elif(user_choice == 'Water' and com == 'Rock') or (user_choice == 'Scissors' and com == 'Paper') or (user_choice == 'Rock' and com == 'Scissors'):
      print("Computer won")
else:
      print("It's a tie")

if __name__ == "__main__":
   main()