import random


rps = ['rock', 'paper', 'scissors']

#takes no parameters, returns the provided user input
def getUserInput():

    userInput = input('What\'s your move? \n').lower()
    while userInput not in rps:
        userInput = input('Try again... what\'s your move?').lower()
    return userInput

#takes no input parameters, returns the choice
def chooseMove():

    return random.choice(rps)

#takes as input the computers move and the players move, and returns draw, win, or lose
def chooseWinner(playerMove, computerMove):
    if playerMove == 'rock' and computerMove == 'rock':
        return 'draw'
    elif playerMove == 'rock' and computerMove == 'scissors':
        return 'win'
    elif playerMove == 'rock' and computerMove == 'paper':
        return 'lose'
    
    elif playerMove == 'scissors' and computerMove == 'rock':
        return 'lose'
    elif playerMove == 'scissors' and computerMove == 'scissors':
        return 'draw'
    elif playerMove == 'scissors' and computerMove == 'paper':
        return 'win'
    elif playerMove == 'paper' and computerMove == 'rock':
        return 'win'
    elif playerMove == 'paper' and computerMove == 'scissors':
        return 'lose'
    elif playerMove == 'paper' and computerMove == 'paper':
        return 'draw'

#Main loop plays to best 2 out of 3 and keeps score

def play():

    wins = 0
    losses = 0   
    
    while wins != 2 and losses!= 2:
        userChoice = getUserInput()
        computerChoice = chooseMove()
        if chooseWinner(userChoice, computerChoice) == 'win':
            wins += 1

            print(f'Computer chose {computerChoice}, you win!')
        elif chooseWinner(userChoice, computerChoice) == 'lose':
            losses +=1

            print(f'Computer chose {computerChoice}, you lost.')
        else:
            print(f'Computer chose {computerChoice}, it\'s a draw.')
        print(f'Score is {wins} to {losses}')
    print(wins, losses)
    if wins == 2:
        print('You win!')
    else:
        print('You lose!')
    

play()

