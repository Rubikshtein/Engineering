import requests

# import html to strip html encoding from the response
import html

import random
import json

# Get trivia questions function - takes 2 parameters (amount of questions & category as int), returns a list
def get_questions(amount: int, category: int) -> list:
    # url from trivia.py file where amount and category integers are replaced with variables
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    # get json response for content
    response_json = response.json()
    # filter out boolean type questions
    filtered_questions = [question for question in response_json["results"] if question["type"] != "boolean"]
    return filtered_questions

# Shuffle answers function - takes one parameter (answer choices for each question as ls), returns a list
"""
Correct and incorrect questions are separate items in trivia dictionary so when printed, 
the correct answer is displayed separately, which can expose the correct answer.
"""
def shuffle(choices: list) -> list:
    # shuffle function from random module
    random.shuffle(choices)
    return choices

# Print numbered answer choices function - takes one parameter (answer choices for each question as ls), no return
def print_choices(choices: list) -> None:
    # enumerate answer choices
    for choice_index, choice in enumerate(choices):
        # remove html characters and change choice indexing so that enumeration starts from 1
        print(f"{choice_index+1}. {html.unescape(choice)}")

# Get user choice function - takes no parameters, returns an int
def get_user_choice() -> int:
    # validate user input
    while True:
        # store user answer and convert into an integer
        user_choice = int(input("Enter the number of your answer: "))
        # validate user input (4 answers per question only)
        if user_choice in range(1, 5):
            # remove 1 from user answer number to match answer choice index enumerated previously
            return user_choice - 1
        else:
            print("Invalid input. Enter the number of your answer: ")

# Write result into a file function - takes four parameters (filename, result, score, total questions), no return
def record_result(filename: str, result: list, score: int, total: int) -> None:
    # mode can be changed to 'a' to keep track of all games
    with open(filename, 'w') as text:
        # total number of questions in the game
        total = len(result)
        # loop through result items and write each on a new line
        for item in result:
            text.write(f'Question: ' + item['question'] + '\n')
            text.write('\n')
            text.write(f'User answer: ' + item['user_answer'] + '\n')
            text.write(f'Correct answer: ' + item['correct_answer'] + '\n')
            text.write('\n')
        # write user score for all questions
        text.write(f'Final score: {score} out of {total}\n')

# Play the trivia game (main function) - takes two parameters (amount & category as int), no return
def play_trivia(amount: int, category: int) -> None:
    # call the get questions function
    questions = get_questions(amount, category)
    # initial score
    score = 0
    # empty list to store results
    result = []
    # total number of questions in the game
    total = len(result)

    # loop through questions
    for question in questions:
        # question string stripped of html encoding
        question_text = html.unescape(question["question"])
        print(question_text)

        # incorrect answers string
        choices = question["incorrect_answers"]
        # add correct answer to incorrect answers
        choices.extend([question["correct_answer"]])
        # shuffled answers string - calls shuffle choices function
        shuffled_choices = shuffle(choices)
        print_choices(shuffled_choices)

        # user answer as int - calls get user choice
        user_choice_index = get_user_choice()
        # user answer string - assigns answer choice string from choices based on user answer as int
        user_choice_text = shuffled_choices[user_choice_index]

        # correct answer string without html characters
        correct_answer_text = html.unescape(question["correct_answer"])
        # check if user answer matches the correct answer
        if user_choice_text == correct_answer_text:
            print(f"Correct! You answered: {correct_answer_text}\n")
            # add point to the score
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer_text}\n")

        # add game result to result list - questions, user answers and correct answers
        result.append({
            # remove '?' from all questions
            "question": question_text[:-1],
            "user_answer": user_choice_text,
            "correct_answer": correct_answer_text
        })

    # call record result function - 4 parameters (filename, result, score, total)
    record_result("scores.txt", result, score, total)

    # display final score in the console
    print(f"Final score: {score}")

# Play trivia game function
# protect code when imported
if __name__ == "__main__":
    # set amount of questions and category - used as parameters
    amount = 10
    category = 9
    # call main function
    play_trivia(amount, category)