import random
DIFFICULTY_RANGES = {
    "easy": (1,50),
    "medium": (1,200),
    "hard": (1,500)
}
level = input("Choose difficulty (easy/medium/hard): ").strip().lower()
if level not in DIFFICULTY_RANGES:
    print("Invalid choice, defaulting to easy.")
    level = "easy"
start, end = DIFFICULTY_RANGES[level]
pick = random.randint(start, end)
attempts = 0

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == pick:
        print(f"🎉 Correct! You got it in {attempts} attempts.")
        break
    elif guess < pick:
        print("Too low, try again")
    else:
        print("Too high, try again")