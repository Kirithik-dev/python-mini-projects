# 🎮 Quiz Arena

A terminal-based Python quiz game with **difficulty levels** and a **per-question timer**. Questions are loaded from a JSON file, so you can easily add, edit, or expand the question bank without touching the game logic.

## Features

- ✅ Multiple-choice questions loaded from `questions.json`
- ⏱ Timed answers — time limit depends on question difficulty (easy = more time, hard = less)
- 🎚 Choose to play **easy**, **medium**, **hard**, or **all** questions
- 📊 Score tracking with a final result summary
- ❌ Graceful handling of invalid or missed (timed-out) answers

## How It Works

1. Questions are stored in `questions.json`, each with:
   - `question` — the question text
   - `options` — list of possible answers
   - `answer` — the correct answer
   - `difficulty` — `easy`, `medium`, or `hard`
2. On start, the player picks a difficulty (or plays all questions).
3. Each question is shown with a countdown limit based on its difficulty.
4. Answers are validated, scored, and a final score is shown at the end.

## Getting Started

### Prerequisites
- Python 3.x installed

### Run it

```bash
# clone the repo (if you haven't already)
git clone https://github.com/<your-username>/python-mini-projects.git
cd python-mini-projects/quiz_game

# run the game
python guess.py
```

### Example

```
🎮 Hey genius, welcome to the Quiz Arena! Let's see if that brain of yours is as sharp as you think 😏
DO YOU WANT TO PLAY THE GAME (Y/N): y
Choose difficulty (easy/medium/hard/all): medium

[MEDIUM] What is the time complexity of binary search?  (⏱ 8s)
---1---O(n)
---2---O(n log n)
---3---O(log n)
---4---O(1)
Your answer (enter option number): 3
✅ Correct!
```

## Project Structure

```
quiz_game/
├── guess.py        # main game logic
├── questions.json   # question bank
└── README.md
```

## Possible Improvements

- Save high scores to a file / leaderboard
- Category-based question selection (e.g. Python, DSA, General Knowledge)
- GUI version using Tkinter
- Negative marking / streak bonuses

## Author

Built by **Kirithik** as part of a personal Python mini-projects collection.