import random

def play():
    user = input("What's your choice? Pick 'r' for rock, 's' for scissor and 'p' for paper\n")
    computer = random.choice(['r','s','p'])

    if computer == user:
        return 'It\'s a TIE!'

    if is_win(user,computer):
        return 'Congrats! You won!'
    else:
        return 'Better Luck Next Time!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
