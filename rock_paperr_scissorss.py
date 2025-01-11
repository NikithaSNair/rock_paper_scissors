import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
        outcomes = {
        ("rock", "scissors"): "You win! Rock crushes Scissors.",
        ("scissors", "paper"): "You win! Scissors cuts Paper.",
        ("paper", "rock"): "You win! Paper covers Rock.",
        ("scissors", "rock"): "You lose! Rock crushes Scissors.",
        ("paper", "scissors"): "You lose! Scissors cuts Paper.",
        ("rock", "paper"): "You lose! Paper covers Rock.",
    }
    
    if player_choice == computer_choice:
        return "TIE!!!!!
    return outcomes.get((player_choice, computer_choice), "Invalid choice!")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please choose rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)
play_game()
