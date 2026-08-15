import os
import random
import json

STATS_FILE = "stats.json"

RULES = {
  "rock": ["scissors", "lizard"],
  "paper": ["rock", "spock"],
  "scissors": ["paper", "lizard"],
  "lizard": ["paper", "spock"],
  "spock": ["rock", "scissors"]
}

CHOICES = list(RULES.keys())

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"matches_played": 0, "player_match_wins": 0, "computer_match_wins": 0}
    try:
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Stats file looked corrupted, starting fresh.")
        return {"matches_played": 0, "player_match_wins": 0, "computer_match_wins": 0}

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def get_choice_input():
    options_str = "/".join(CHOICES)
    while True:
        choice = input(f"Choose ({options_str}): ").strip().lower()
        if choice in CHOICES:
            return choice
        print(f"Invalid choice — pick one of: {options_str}")

def get_best_of_input():
    while True:
        raw = input("Best of how many rounds? (3/5/7): ").strip()
        if raw in ("3", "5", "7"):
            return int(raw)
        print("Please choose 3, 5, or 7.")

def play_round(player_choice):
    computer_choice = random.choice(CHOICES)
    print(f"You chose {player_choice}, I chose {computer_choice}.")
 
    if player_choice == computer_choice:
        print("🤝 It's a tie!")
        return "tie"
    elif computer_choice in RULES[player_choice]:
        print(f"✅ {player_choice.capitalize()} beats {computer_choice}. You win this round!")
        return "player"
    else:
        print(f"❌ {computer_choice.capitalize()} beats {player_choice}. I win this round!")
        return "computer"

def play_match(best_of, stats):
    rounds_to_win = (best_of // 2) + 1
    player_score = 0
    computer_score = 0
    round_num = 1
 
    print(f"\nMatch started — first to {rounds_to_win} round wins takes it!")
 
    while player_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\n--- Round {round_num} ---")
        player_choice = get_choice_input()
        result = play_round(player_choice)
 
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
 
        print(f"Score — You: {player_score}  |  Computer: {computer_score}")
        round_num += 1
 
    stats["matches_played"] += 1
    if player_score > computer_score:
        print(f"\n🏆 You won the match {player_score}-{computer_score}!")
        stats["player_match_wins"] += 1
    else:
        print(f"\n💻 Computer won the match {computer_score}-{player_score}.")
        stats["computer_match_wins"] += 1
    save_stats(stats)
 
 
def main():
    print("=" * 60)
    print("🪨📄✂️ Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    print("=" * 60)
 
    stats = load_stats()
    print(f"Matches played: {stats['matches_played']} "
          f"(You: {stats['player_match_wins']}  |  Computer: {stats['computer_match_wins']})")
 
    while True:
        choice = input("\n1. Play a match\n2. Quit\n> ").strip()
 
        if choice == '1':
            best_of = get_best_of_input()
            play_match(best_of, stats)
        elif choice == '2':
            print("Thanks for playing 👋")
            break
        else:
            print("Please enter 1 or 2")
 
 
if __name__ == "__main__":
    main()
 
