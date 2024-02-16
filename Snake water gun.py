# Import necessary library
import random

# Display a welcome message for the Snake Water Gun game
print("WELCOME TO SNAKE WATER GUN GAME\nIT WILL BE A GAME OF 3 ROUNDS\n")

# Get user consent to play the game
consent = input("Are you ready to play (type 'y' or 'n')?")

# Check if the user is ready to play
if consent == "y":
    # Dictionary to map choices to their corresponding names
    Choices = {1: "Snake", 2: "Water", 3: "Gun"}
    
    # Initialize scores for the player and computer
    You = 0
    Computer = 0
    
    # Loop for 3 rounds of the game
    for i in range(3):
        # Get user input for their choice
        user_input = int(input("Enter your choice\n1. Snake\n2. Water\n3. Gun\n"))
        print(f"You chose: {Choices[user_input]}")  

        # Generate a random choice for the computer
        computer_input = random.randint(1, 3)
        print(f"Computer chose: {Choices[computer_input]}")

        # Determine the winner of the round
        if user_input == computer_input:
            print("Draw\nLet's play again")
        elif user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
            print("You win\nNext Round")
            You += 1
        elif user_input == 2 and computer_input == 1 or user_input == 3 and computer_input == 2 or user_input == 1 and computer_input == 3:
            print("Computer wins\nNext Round")
            Computer += 1

    # Display final scores
    print("Your score is:", You)
    print("Computer score is:", Computer)

    # Determine the overall winner of the game
    if You > Computer:
        print("You won the game")
    elif You == Computer:
        print("The game is a draw")
        # Ask if the user wants to play again in case of a draw
        consent2 = input("Do you want to play again (type 'y' or 'n')?")
        if consent2 == "y":
            # Reset scores for a new game
            You = 0
            Computer = 0
            # Continue the game loop for 3 rounds
            for i in range(3):
                user_input = int(input("Enter your choice\n1. Snake\n2. Water\n3. Gun\n"))
                print(f"You chose: {Choices[user_input]}")  

                computer_input = random.randint(1, 3)
                print(f"Computer chose: {Choices[computer_input]}")

                if user_input == computer_input:
                    print("Draw\nLet's play again")
                elif user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
                    print("You win\nNext Round")
                    You += 1
                elif user_input == 2 and computer_input == 1 or user_input == 3 and computer_input == 2 or user_input == 1 and computer_input == 3:
                    print("Computer wins\nNext Round")
                    Computer += 1

            # Display final scores for the second round
            print("Your score is:", You)
            print("Computer score is:", Computer)
            
            # Determine the overall winner of the second round
            if You > Computer:
                print("You won the game")
            elif You == Computer:
                print("The game is a draw")
                # Ask if the user wants to play again in case of a draw
                consent3 = input("Do you want to play again (type 'y' or 'n')?")
                if consent3 == "y":
                    # Reset scores for a new game
                    You = 0
                    Computer = 0
                    # Continue the game loop for 3 rounds
                    for i in range(3):
                        user_input = int(input("Enter your choice\n1. Snake\n2. Water\n3. Gun\n"))
                        print(f"You chose: {Choices[user_input]}")  

                        computer_input = random.randint(1, 3)
                        print(f"Computer chose: {Choices[computer_input]}")

                        if user_input == computer_input:
                            print("Draw\nLet's play again")
                        elif user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
                            print("You win\nNext Round")
                            You += 1
                        elif user_input == 2 and computer_input == 1 or user_input == 3 and computer_input == 2 or user_input == 1 and computer_input == 3:
                            print("Computer wins\nNext Round")
                            Computer += 1

                    # Display final scores for the third round
                    print("Your score is:", You)
                    print("Computer score is:", Computer)
                    
                    # Determine the overall winner of the third round
                    if You > Computer:
                        print("You won the game")
                    elif You == Computer:
                        print("The game is a draw")
                        # Ask if the user wants to play again in case of a draw
                        consent4 = input("Do you want to play again (type 'y' or 'n')?")
                        if consent4 == "y":
                            # Continue the game loop for 3 rounds
                            for i in range(3):
                                user_input = int(input("Enter your choice\n1. Snake\n2. Water\n3. Gun\n"))
                                print(f"You chose: {Choices[user_input]}")  

                                computer_input = random.randint(1, 3)
                                print(f"Computer chose: {Choices[computer_input]}")

                                if user_input == computer_input:
                                    print("Draw\nLet's play again")
                                elif user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
                                    print("You win\nNext Round")
                                    You += 1
                                elif user_input == 2 and computer_input == 1 or user_input == 3 and computer_input == 2 or user_input == 1 and computer_input == 3:
                                    print("Computer wins\nNext Round")
                                    Computer += 1

                            # Display final scores for the fourth round
                            print("Your score is:", You)
                            print("Computer score is:", Computer)
                            
                            # Determine the overall winner of the fourth round
                            if You > Computer:
                                print("You won the game")
                            elif You == Computer:
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
            print("Thank you for playing")
    else:
