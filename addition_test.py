import random

QUESTION = 5

def addition_test():
    for question in range(1, QUESTION + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print('Question', question)
        print('num1 + num2 =', num1, '+', num2, '= _____')
        print()

addition_test()