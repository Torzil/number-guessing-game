from random import randint

print("============================ Welcome to the number guessing game! ============================")
print("The computer has chosen a random number from 1 to 100. Can you guess it in less than 5 tries?")

generated_number = randint(1, 100)
tries = 1

while True:
    if tries > 5:
        print("You ran out of tries! Better luck next time.")
        break
    player_guess = input("Guess a number: ")
    if not player_guess.isdigit():
        print("Invalid input! Please try again.")
        continue
    if int(player_guess) == generated_number:
        if tries == 1:
            print("Amazing! You guessed the number on your first try!")
        else:
            print(f"Congratulations! You guessed the number in {tries} tries.")
        break
    else:
        if int(player_guess) > generated_number:
            print("Wrong number! Go lower.")
        elif int(player_guess) < generated_number:
            print("Wrong number! Go higher.")
    tries += 1
