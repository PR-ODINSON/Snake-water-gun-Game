import random
print("WELCOME TO SNAKE WATER GUN GAME\nIT WILL A GAME OF 3 ROUNDS\n")
consent=input("Are you ready to play(type y or n)?")
if consent=="y":
  Choices={1:"Snake",2:"Water",3:"Gun"}
  You=0
  Computer=0
  for i in range(3):
    user_input=int(input("Enter your choice\n1.Snake\n2.Water\n3.Gun\n"))
    print(f"You chose: {Choices[user_input]}")  
    
    
    computer_input=random.randint(1,3)
    print(f"Computer chose: {Choices[computer_input]}")
    

    if user_input==computer_input:
      print("Draw\nLet's play again")
    elif user_input==1 and computer_input==2 or user_input==2 and computer_input==3 or user_input==3 and computer_input==1:
      print("You win\nNext Round")
      You+=1
    elif user_input==2 and computer_input==1 or user_input==3 and computer_input==2 or user_input==1 and computer_input==3:
      print("Computer wins\nNext Round")
      Computer+=1

  print("Your score is:",You)
  print("Computer score is:",Computer)
  if You>Computer:
    print("You won the game")
  elif You==Computer:
    print("The game is a draw")
    consent2=input("Do you want to play again(type y or n)?")
    if consent2=="y":
      You=0
      Computer=0
      for i in range(3):
        user_input=int(input("Enter your choice\n1.Snake\n2.Water\n3.Gun\n"))
        print(f"You chose: {Choices[user_input]}")  


        computer_input=random.randint(1,3)
        print(f"Computer chose: {Choices[computer_input]}")

        if user_input==computer_input:
          print("Draw\nLet's play again")
        elif user_input==1 and computer_input==2 or user_input==2 and computer_input==3 or user_input==3 and computer_input==1:
          print("You win\nNext Round")
          You+=1
        elif user_input==2 and computer_input==1 or user_input==3 and computer_input==2 or user_input==1 and computer_input==3:
          print("Computer wins\nNext Round")
          Computer+=1

      print("Your score is:",You)
      print("Computer score is:",Computer)
      if You>Computer:
        print("You won the game")
      elif You==Computer:
        print("The game is a draw")
        consent3=input("Do you want to play again(type y or n)?")
        if consent3=="y":
          You=0
          Computer=0
          for i in range(3):
            user_input=int(input("Enter your choice\n1.Snake\n2.Water\n3.Gun\n"))
            print(f"You chose: {Choices[user_input]}")  


            computer_input=random.randint(1,3)
            print(f"Computer chose: {Choices[computer_input]}")


            if user_input==computer_input:
              print("Draw\nLet's play again")
            elif user_input==1 and computer_input==2 or user_input==2 and computer_input==3 or user_input==3 and computer_input==1:
              print("You win\nNext Round")
              You+=1
            elif user_input==2 and computer_input==1 or user_input==3 and computer_input==2 or user_input==1 and computer_input==3:
              print("Computer wins\nNext Round")
              Computer+=1

          print("Your score is:",You)
          print("Computer score is:",Computer)
          if You>Computer:
            print("You won the game")
          elif You==Computer:
            print("The game is a draw")
            consent4=input("Do you want to play again(type y or n)?")
            if consent4=="y":
              for i in range(3):
                user_input=int(input("Enter your choice\n1.Snake\n2.Water\n3.Gun\n"))
                print(f"You chose: {Choices[user_input]}")  


                computer_input=random.randint(1,3)
                print(f"Computer chose: {Choices[computer_input]}")

                if user_input==computer_input:
                  print("Draw\nLet's play again")
                elif user_input==1 and computer_input==2 or user_input==2 and computer_input==3 or user_input==3 and computer_input==1:
                  print("You win\nNext Round")
                  You+=1
                elif user_input==2 and computer_input==1 or user_input==3 and computer_input==2 or user_input==1 and computer_input==3:
                  print("Computer wins\nNext Round")
                  Computer+=1

              print("Your score is:",You)
              print("Computer score is:",Computer)
              if You>Computer:
                print("You won the game")
              elif You==Computer:
                print("The game is a draw\nYour Trials are over")
              else:
                print("Computer won the game")
            else:
              print("Thank you for playing")
          else:
            print("Thank you for playing")
        else:
          print("Thank you for playing")
      else:
        print("Computer won the game")
  else:
    print("Computer won the game")
else:
  print("Thank you for visiting")
    
  
