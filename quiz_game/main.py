# ask question
# check for result
# update score

import data
from question_model import AskQues
from quiz_brain import CheckAns, ScoreChecker


askques = AskQues()
score = ScoreChecker()
check_ans1 = CheckAns()

is_true = True
while is_true:
    ques = data.question_data
    print("Welcome to prince Quiz: ")
    for i in range(1, 11):
        question = ques.pop()
        print(f"Q.{i}.{askques.get_ques(question)}?\n True/False: ")
        user_input = input().capitalize()
        answer = askques.get_ans(question)
        result = check_ans1.check_ans(user_input, answer)
        score.update_score(result)
        if result:
            print("You got it right: ")
            print(f"your current score is: {score.get_score()}/{i}.\n\n\n")
        else:
            print("Thats Wrong: ")
            print(f"your current score is: {score.get_score()}/{i}.\n\n\n")
            break
    play_again = input(
        "Do you want to play again:\nType 'y' for playing again else any key to exit : ")
    print("\n\n\n")
    if play_again.lower() == "y":
        is_true = True
    else:
        is_true = False
