import random
from list import *
# Questions and answers                 


def populate_list():
  pass


def play_game():
    # Select a random question
    question_index = random.randint(0, 3)
    question = player1_questions[question_index]
    possible_answers = player1_answers[question_index]
    print("\nQuestion:", question)

    # Shuffle the answers
    random.shuffle(possible_answers)

    # Get user's choice
    user_choice = input("Your answer: ")
    if user_choice.lower == possible_answers:
      print("\nYou got it right!")
    else:
      print("\nYou got it wrong. The possible answers were:", possible_answers)
  
    # Check if the answer is correct
   





#main part

print("Welcome to our Family Feud Game. You will get asked 4 questions. The answers are from data we collected from a hundred people. Every correctly answered question will be one point. You can play this game in total as four players. Please answer all the question in lower case.")

# Main loop
while True:
    play_game()
    #play_again = input("Do you want to play again? (yes/no): ")
    #if play_again.lower() != "yes":
        #break


  



#print("Thank you for playing!")