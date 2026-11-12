from random import randint
from input_handler import get_valid_guess

while True:
    secret_num = randint(1, 100)

    attempts = 0

    while True:
        user_num = get_valid_guess()

        attempts += 1

        if user_num > secret_num:
            print("Wrong! Too high...")

        elif user_num < secret_num:
            print("Wrong! Too low...")

        else:
            print(f"That's right! Random number is {secret_num}")
            break

    print(f"You've needed {attempts} attempts")

    while True:
        play_again = input("Do you want to play again? (y,n) ").lower()
        if play_again != 'y' and play_again != 'n':
            print("You must enter y or n!")
            continue
        break

    if play_again == 'y':
        continue
    else:
        break
