import json
import time
import threading

with open("questions.json", 'r') as f:
    data = json.load(f)
questions = data['questions']

print('-'*100)
print("🎮 Hey genius, welcome to the Quiz Arena! Let's see if that brain of yours is as sharp as you think 😏")
print('-'*100)

score = 0

# time limit (seconds) per difficulty
TIME_LIMITS = {"easy": 10, "medium": 8, "hard": 6}

def get_timed_input(prompt, limit):
    """Returns user input, or None if they took too long."""
    answer = [None]

    def take_input():
        answer[0] = input(prompt)

    t = threading.Thread(target=take_input)
    t.daemon = True
    t.start()
    t.join(timeout=limit)
    return answer[0]

while True:
    a = input("DO YOU WANT TO PLAY THE GAME (Y/N): ").strip().lower()
    if a == 'y':
        level = input("Choose difficulty (easy/medium/hard/all): ").strip().lower()

        if level in ("easy", "medium", "hard"):
            selected_questions = [q for q in questions if q['difficulty'] == level]
        else:
            selected_questions = questions

        if not selected_questions:
            print("No questions found for that difficulty. Try again.")
            continue

        for quest in selected_questions:
            limit = TIME_LIMITS[quest['difficulty']]
            print(f"\n[{quest['difficulty'].upper()}] {quest['question']}  (⏱ {limit}s)")
            for index, opt in enumerate(quest['options']):
                print(f"---{index+1}---{opt}")

            answer = get_timed_input("Your answer (enter option number): ", limit)

            if answer is None:
                print("⏰ Time's up!")
                chosen = None
            else:
                try:
                    chosen = quest['options'][int(answer) - 1]
                except (ValueError, IndexError):
                    chosen = None

            if chosen == quest['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {quest['answer']}\n")

        print(f"🏁 Game over! Your final score: {score}/{len(selected_questions)}")
        break
    elif a == 'n':
        print("Alright, maybe next time 👋")
        break
    else:
        print("Please enter Y or N")