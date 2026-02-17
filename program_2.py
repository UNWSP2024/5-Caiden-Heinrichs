#Week 5, Program 2 - Math Quiz
#Caiden Heinrichs
#02/20/26

import random

#This function checks if the user answer is correct
def check_answer(number1, number2, user_answer):
    return number1 + number2 == user_answer


def main():
    #Generate the random numbers
    number1 = random.randint(100, 999)
    number2 = random.randint(100, 999)

    #Ask the user to solve the question
    print("What is", number1, "+", number2, "?")
    user_answer = int(input())
    
    #Check if the user answer is correct and provide feedback
    if check_answer(number1, number2, user_answer):
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect; the correct answer is", number1 + number2)


if __name__ == '__main__':
    main()
