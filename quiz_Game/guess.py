import json
with open("questions.json",'r') as f:
  data = json.load(f)
questions = data['questions']
print('-'*100)
print("🎮 Hey genius, welcome to the Quiz Arena! Let's see if that brain of yours is as sharp as you think 😏")
print('-'*100)
score = 0
while True:
  a = input("DO YOU WANT TO PLAY THE GAME (Y/N): ").strip().lower()
  if a=='y':
    for quest in questions:
      print(quest['question'])
      for index,opt in enumerate(quest['options']):
        print(f"---{index+1}---{opt}")
      answer = input("Your answer (enter option number) : ").strip()
      try:
        chosen = quest['options'][int(answer)-1]
      except (ValueError, IndexError):
        chosen = None
      if chosen == quest['answer']:
        print("✅ Correct!\n")
        score+=1
      else:
        print(f"❌ Wrong! The correct answer was: {quest['answer']}\n")
    print(f"🏁 Game over! Your final score: {score}/{len(questions)}")
    break
  elif a=='n':
    print("Alright, maybe next time 👋")
    break
  else:
    print("Please enter Y or N")






  