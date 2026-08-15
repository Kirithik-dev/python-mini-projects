# 🎯 Guess or Be Guessed

A number guessing game with a twist — you can either guess the computer's number, or flip it around and have the **computer guess yours using binary search**. Includes difficulty levels and persistent stats saved across sessions.

## Features

- 🔢 **Mode 1 — You guess the number**: computer picks a random number in a range you choose (easy/medium/hard), you guess with higher/lower hints
- 🤖 **Mode 2 — Computer guesses your number**: you think of a number between 1-100, the computer finds it using **binary search**, always solving it in at most 7 guesses
- 📊 Persistent stats — games played, wins, and best attempt count are saved to `stats.json` and shown on every launch
- 🛡 Input validation — invalid or out-of-range input won't crash the game, it just re-prompts
- 🎚 Difficulty-based ranges: easy (1-50), medium (1-200), hard (1-500)

## Why Binary Search?

Mode 2 isn't just guess-and-check — the computer always guesses the **midpoint** of the current possible range, then narrows the range based on your "higher/lower" response, cutting the search space in half each time. For a range of 1-100, this guarantees a solve in at most **⌈log₂(100)⌉ = 7 guesses**, no matter what number you pick.


## Example

```
🎯 Welcome to Guess or Be Guessed!
You've played 3 games so far (you won 2, I won 1).

Choose mode:
1. You guess the number
2. I'll guess your number
3. Quit
> 2

Think of a number between 1 and 100. I'll try to guess it!
Press Enter when you're ready...
Is your number 50? (h = too high, l = too low, c = correct): l
Is your number 75? (h = too high, l = too low, c = correct): c
🎉 I guessed it in 2 attempts! Your number was 75.
```

## Project Structure

```
guess-or-be-guessed/
├── game.py         # game logic (both modes, stats, validation)
├── stats.json       # auto-created on first run, tracks player/computer stats
└── README.md
```

## Possible Improvements

- Track a rolling history of past games, not just best/total counts
- Add a "liar mode" where hints are occasionally wrong on purpose
- GUI version showing the shrinking search range visually
- Global leaderboard if ever turned into a web app

## Author

Built by **Kirithik** as part of a personal Python mini-projects collection.