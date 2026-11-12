def get_valid_guess() -> int:
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