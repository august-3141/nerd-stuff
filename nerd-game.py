# Yay math

# Yes i'm a nerd shut up

import random

print('*** Math Game ***')

qAmount = 0

try:
    qAmount = int(input("How many questions would you like? "))
except:
    print("That's not a valid number!")

qCurrent = 0
operatorList = ['+', '-', '*']
correctCount = 0
incorrectCount = 0

while qCurrent < qAmount:

    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operator = operatorList[random.randint(0, 2)]

    question = f"{num1} {operator} {num2} "
    answer = int(input(f"{question}"))

    if answer == eval(question):
        
        print("Good Job!")
        correctCount = correctCount + 1
    
    else:

        print(f"Sorry, the answer was {eval(question)}!")
        incorrectCount = incorrectCount + 1
        

    qCurrent = qCurrent + 1

print(f'You got {correctCount} right and {incorrectCount} wrong. That\'s {correctCount / qAmount * 100}% accuracy!')

if (correctCount / qAmount * 100) >= 70:
    print('Nice work on the quiz!')
else:
    print('There\'s always next time!')