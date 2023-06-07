import random
from list import *
# Questions and answers                 

global score
score = 0
def populate_list():
  pass


def play_game():
  global score
  # Select a random question
  length_of_list = len(player1_questions)-1
  question_index = random.randint(0, length_of_list)
  print("Question index chosen:",question_index)
  length_of_list_answers = len(player1_answers)
  question = player1_questions[question_index]
  possible_answers = player1_answers[question_index]
  print("\nQuestion:", question)

  # Shuffle the answers
  random.shuffle(possible_answers)

  # Get user's choice
  user_choice = input("Your answer: ")
  if user_choice.lower() in possible_answers:
    print("\nYou got it right!")
    score +=1
    print(f"Your score is {score}")
    print(player1_questions)
    print(player1_answers)
    player1_questions.remove(player1_questions[question_index])
    player1_answers.remove(player1_answers[question_index])
  else:
    print(f"\nYou got it wrong. You guessed {user_choice}. The possible answers were:", possible_answers)

  






#main part

print("Welcome to our Family Feud Game. You will get asked 4 questions. The answers are from data we collected from a hundred people. Every correctly answered question will be one point. You can play this game in total as four players. Please answer all the question in lower case.")


while True:
    play_game()
    
  


play_again = input("\nDo you want to play again? (yes/no): ")
if play_again.lower() != "yes":
    play_game()
else:
  print("Thank you for playing!")