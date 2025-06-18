import random

wins = 0
losses = 0

while True:
    
    guess = input("Guess a number from 1 to 9 (or type 'quit' to stop): ")
    
    if guess.lower() == "quit":
        break  

    if not guess.isdigit() or not (1 <= int(guess) <= 9):
        print("Please enter a valid number between 1 and 9.")
        continue  
    
    guess = int(guess)
    random_number = random.randint(1, 9)
    
    if guess == random_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time. The correct number was {random_number}.")
        losses += 1


print(f"\nGames won: {wins}")
print(f"Games lost: {losses}")
print("Thanks for playing!")
