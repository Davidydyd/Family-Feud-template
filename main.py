import random
from list import*
# Questions and answers                 


def populate_list():
  pass


def play_game():
    # Select a random question
    question_index = random.randint(0, len(questions) - 1)
    question = questions[question_index]
    possible_answers = answers[question_index]

    print("Question:", question)

    # Shuffle the answers
    random.shuffle(possible_answers)

    # Get user's choice
    user_choice = input("Your answer:")
  
    # Check if the answer is correct
   

# Main loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thank you for playing!")