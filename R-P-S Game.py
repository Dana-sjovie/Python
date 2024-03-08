import random


def play():
    user = input ("What you going with? 'R'for rock  'P' for paper 'S' for scissors\n" )
    computer = random.choice({'R' , 'P' , 'S'})

    if user == computer:
        return 'Close but it\'s a draw'
    
    if is_win(user, computer):
        return "YOU WON!"
    
    return "You lost"

def is_win (player, opponent):

    if (player == "R" and opponent == "S") or (player == "S" and opponent == "P" ) \
        or (player == "p" and opponent == "R"):
        return True

        print((play))