import random
def play_game():

    game_round = 1
    score = 0
    options = ["rock", "paper", "scissors"]
    
    while game_round <= 3:

        print(f"Round:{game_round}")
        computer = random.choice(options)
        user = input("Type rock papar or scissors: ").lower()

        if user not in options:
            print("Input invalid.Try again\n")
            continue

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        if user == computer:
            print("Its a tye")
        elif (user == "rock" and computer == "scissors") or  (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            print("You won")
            score += 1
        else:
            print("you lost")
            score -= 1

        print(f"Your score is {score}\n")
        game_round += 1
        
    print(f"Game over\n Your final score is:{score}")
    
   
play_game()
