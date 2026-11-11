from random import randint


def get_valid_guess():
    while True:
        try:
            num = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("You must enter a number!")
            continue

        if num < 1 or num > 100:
            print("Your number must be between 1 and 100!")
            continue

        return num


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
