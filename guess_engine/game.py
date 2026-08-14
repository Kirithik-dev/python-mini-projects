import random
import json
import os

STATS_FILE = "stats.json"
 
DIFFICULTY_RANGES = {
    "easy": (1, 50),
    "medium": (1, 200),
    "hard": (1, 500)
}

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {
            "games_played": 0,
            "player_wins": 0,
            "player_best_attempts": None,
            "computer_wins": 0,
            "computer_best_attempts": None
        }
    with open(STATS_FILE, 'r') as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def player_guess(start, end, stats):
    pick = random.randint(start, end)
    attempts = 0
    print(f"I've picked a number between {start} and {end}. Try to guess it!")
 
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
 
        if guess == pick:
            print(f"🎉 Correct! You got it in {attempts} attempts.")
            stats["games_played"] += 1
            stats["player_wins"] += 1
            if stats["player_best_attempts"] is None or attempts < stats["player_best_attempts"]:
                stats["player_best_attempts"] = attempts
                print("🏆 New personal best!")
            save_stats(stats)
            break
        elif guess < pick:
            print("Too low, try again")
        else:
            print("Too high, try again")

def computer_guess(start, end, stats):
    print(f"\nThink of a number between {start} and {end}. I'll try to guess it!")
    input("Press Enter when you're ready...")
 
    attempts = 0
    while start <= end:
        mid = (start + end) // 2
        attempts += 1
        response = input(f"Is your number {mid}? (h = too high, l = too low, c = correct): ").strip().lower()
 
        if response == 'c':
            print(f"🎉 I guessed it in {attempts} attempts! Your number was {mid}.")
            stats["games_played"] += 1
            stats["computer_wins"] += 1
            if stats["computer_best_attempts"] is None or attempts < stats["computer_best_attempts"]:
                stats["computer_best_attempts"] = attempts
                print("🏆 New best for the computer!")
            save_stats(stats)
            break
        elif response == 'h':
            end = mid - 1
        elif response == 'l':
            start = mid + 1
        else:
            print("Please enter h, l, or c")
            attempts -= 1
    else:
        print("Hmm, that's not possible... did you give me a wrong hint somewhere? 🤔")

def main():
    print("🎯 Welcome to Guess or Be Guessed!")
    stats = load_stats()
    print(f"You've played {stats['games_played']} games so far "
          f"(you won {stats['player_wins']}, I won {stats['computer_wins']}).")
 
    while True:
        choice = input("\nChoose mode:\n1. You guess the number\n2. I'll guess your number\n3. Quit\n> ").strip()
 
        if choice == '1':
            level = input("Choose difficulty (easy/medium/hard): ").strip().lower()
            if level not in DIFFICULTY_RANGES:
                print("Invalid choice, defaulting to easy.")
                level = "easy"
            start, end = DIFFICULTY_RANGES[level]
            player_guess(start, end, stats)
 
        elif choice == '2':
            computer_guess(1, 100, stats)
 
        elif choice == '3':
            print("Thanks for playing 👋")
            break
 
        else:
            print("Please enter 1, 2, or 3")
 
 
if __name__ == "__main__":
    main()
 