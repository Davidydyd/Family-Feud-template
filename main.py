import random
from list import *
# Questions and answers                 

global score
score = 0
def populate_list():
  pass


def play_game(questions, answers):
  global score
  for i in range(4):  
    # Select a random question
    length_of_list = len(questions)-1
    question_index = random.randint(0, length_of_list)
    length_of_list_answers = len(answers)
    question = questions[question_index]
    possible_answers = answers[question_index]
    print("\nQuestion:", question)
  
    # Shuffle the answers
    random.shuffle(possible_answers)
  
    # Get user's choice
    user_choice = input("Your answer: ")
    if user_choice.lower() in possible_answers:
      print("\nYou got it right!")
      score +=1
      print(f"Your score is {score}")
      questions.remove(questions[question_index])
      answers.remove(answers[question_index])
    else:
      print(f"\nYou got it wrong. You guessed {user_choice}. The possible answers were:", possible_answers)
      print(f"\nYour score is {score}")
  
  






#main part

print("Welcome to our Family Feud Game. You will get asked 4 questions. The answers are from data we collected from a hundred people. Every correctly answered question will be one point. You can play this game in total as four players.")

while True:
  play_game(player1_questions, player1_answers)
  print(f"\nYou finished with a score of {score}")
  score = 0
  play_again = input("\nDo you want the next player to play? (yes/no): ")
  if play_again.lower() == "yes":
    play_game(player2_questions, player2_answers)
    print(f"\nYou finished with a score of {score}")
    score = 0
    play_again = input("\nDo you want the next player to play? (yes/no): ")
  else:
    print("Thank you for playing!")
    break
    if play_again.lower() == "yes":
      play_game(player3_questions, player3_answers)
      print(f"\nYou finished with a score of {score}")
      score = 0
      play_again = input("\nDo you want the next player to play? (yes/no): ")
    else:
      print("Thank you for playing!")
      break
      if play_again.lower() == "yes":
        play_game(player4_questions, player4_answers)
        print(f"\nYou finished with a score of {score}")
        score = 0
        break
      else:
        print("Thank you for playing!")
      break
