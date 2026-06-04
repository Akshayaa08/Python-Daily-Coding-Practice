import random

options = ("rock", "paper", "scissors")
# player = None
# computer = random.choice(options)
running = True 


while running:
    player = None
    computer = random.choice(options)
    
    while player not in options: # this while loop will execute till the program choses the choice in the while loop
        player = input ("Enter the choice (rock, paper, scissors): ").lower()

        print(f"Player:{player:10}")
        print(f"Computer :{computer:10}")

        if player == computer:
            print("Its a tie")
        elif player == "rock" and computer =="scissors":
            print("You won!")
        elif player == "paper" and computer == "rock":
            print("You won!")
        elif player =="scissors" and computer == "paper":
            print("You won!")
        else:
            print("The computer won! and you lost!")

        # play_again = input ("Play again? (y/n): ").lower()
        # if not play_again =="y":
        #     running = False
        if not input ("Play again? (y/n): ").lower() == "y":
            running = False

print("Thanks for playing")