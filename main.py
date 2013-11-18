"""
Desciption: CLI version of Mastermind with numbers
Name: main.py
Purpose: Having fun with numbers
Author: Radu-Bogdan Croitoru
Version: 2
"""

from random import randint

def hasUniqueDigits(testString):
    '''
    testString: string, number compounded by pseudo number generator
    return: integer, the number from testString if this passes validation
            or None
    '''
    if len(testString) == len(set(testString)) and testString[0] is not '0':
        return int(testString)

def outputStatusOfGame(number, guess):
    '''
    number: integer, number generated to be guessed
    guess: integer, number of the user
    return: string, what's the status of the game for current guess
            how many digits are centered and not centered.
    '''
    numberList = map(int, str(number))
    guessList = map(int, str(guess))
    centeredList = []

    for i in range(0, 4):
        centeredList.append(numberList[i] - guessList[i])

    totalCentered = centeredList.count(0)
    totalNotCentered = len([i for i in numberList if i in guessList]) - totalCentered

    return '%d[C]  |  %d[N]' % (totalCentered, totalNotCentered)

def generateRandomNumber():
    '''
    return: integer, unique digits 1023 < number < 9876
    '''
    while True:
        randomNumber = hasUniqueDigits(str(randint(1023, 9876)))
        if randomNumber is not None:
            break
    return randomNumber

def askForNumber():
    '''
    return: integer, the users choice
    '''
    while True:
        userNumber = hasUniqueDigits(raw_input('Test a number: '))
        if userNumber is not None and str(userNumber).isdigit() and len(str(userNumber)) == 4:
            break
    return userNumber

def initializeGame():
    '''
    This function initialize the game and generates a random number
    return: integer, call to generateRandomNumber()
    '''
    print "MASTERMIND! [C] = Digit centered  |  [N] = Digit not centered"
    print "The computer picked a number"
    return generateRandomNumber()

def resetGame():
    '''
    This function restarts the game
    '''
    print "The game has been restarted"
    initializeGame()


def main():
    '''
    Main function of the game
    '''
    randomNumber = initializeGame()
    output = '0'

    while output[0] is not '4':
        guess = askForNumber()
        output =  outputStatusOfGame(randomNumber, guess)
        print output

    print "Congratulations, you guessed the number"

main()
