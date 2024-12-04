import random
def game():
      print('''Welcome to the Number Guessing Game!
      I'm thinking of a number between 1 and 100.
      You have some chances to guess the correct number.
            ''')

      print('''Please select the difficulty level:
      1. Easy (10 chances)
      2. Medium (5 chances)
      3. Hard (3 chances)''')
      print()

      while True:
            choice = input("Enter your choice: ")
            print()
            if choice in ['1', '2', '3']:
                  break
            else:
                  print("Invalid input. Please enter a valid choice.\n")

      if choice == '1':
            level = 'Easy'
            changes = 10
      elif choice == '2':
            level = 'Medium'
            changes = 5
      elif choice == '3':
            level = 'Hard'
            changes = 3
      print(f"Great! You have selected the {level} difficulty level. \nLet's start the game!\n")

      answer = random.randint(1,100)

      while (changes > 0):
            attempt = changes
            while True:
                  player= (input("Enter your guess: "))
                  if player.isdigit():
                        player=int(player)
                        break
                  else:
                        print("Invalid input. Please enter a valid choice.\n")
            if player < answer:
                  print(f"Incorrect! The number is greater than {player}.\n")
                  changes = changes -1
            elif player > answer:
                  print(f"Incorrect! The number is less than {player}.\n")
                  changes = changes -1
            else:
                  print(f"Congratulations! You guessed the correct number in {attempt-changes} attempts.\n")
                  break
            if changes == 0:
                  print(f"You are loss, the answer is {answer}, try again!!!\n")
      while True:
            playAgain = input("Play again ?, Press 1, Exit press 0.\n")
            if playAgain in ['0','1']:
                  break
            else:
                  print("Invalid input. Please enter a valid choice.\n")
      if playAgain == '1':
            return game()
      else:
            print("Bye!!!")
            exit()

game()


