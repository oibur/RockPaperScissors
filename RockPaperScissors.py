import random
import time

def main():
    again = 'yes'
    score = 0
    while again == 'yes':
        hum_choice = decide_hum()
        comp = comp_choice()
        result = decide_result(hum_choice, comp)
        print(f'You choose {hum_choice}.')
        time.sleep(.75)
        print(f'The computer choose {comp}.')
        time.sleep(.75)
        print(f'{result}.')
        time.sleep(.75)
        score += get_score(result)
        again = input(f'Your score is {score}. Would you like to play again: ')
    time.sleep(.75)
    print(f'Thanks for playing, your score was {score}')

def get_score(x):
    if x == 'You Tied':
        return 0
    if x == 'You Lose':
        return -1
    if x == 'You Win':
        return 1

def decide_result(human, computer):
    if human == computer:
        return 'You Tied'
    elif human == 'rock':
        if computer == 'paper':
            return 'You Lose'
        else:
            return 'You Win'
    elif human == 'paper':
        if computer == 'scissors':
            return 'You Lose'
        else:
            return 'You Win'
    elif human == 'scissors':
        if computer == 'rock':
            return 'You Lose'
        else:
            return 'You Win'

def comp_choice():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        return 'rock'
    elif comp_choice == 2:
        return 'paper'
    else:
        return 'scissors'

def decide_hum():
    decide_hum = input("Choose rock, paper or scissors: ").lower()
    while True:
        if decide_hum == 'rock':
            break
        elif decide_hum == 'paper':
            break
        elif decide_hum == 'scissors':
            break
        else:
            decide_hum = input("Invalid response. Choose rock, paper or scissors: ").lower()
    return decide_hum

if __name__ == '__main__':
    main()