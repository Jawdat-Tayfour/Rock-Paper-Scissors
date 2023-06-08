import random

def play():

    user = input("Enter 'R' for rock, 'P' for paper or 'S' for scissors: ").lower() # This line is for user input.

    computer = random.choice(['r','p','s']) # here we randomize a computer response.
    if user == computer:
        return "It's a tie!"
    if who_wins(user,computer):
        return "You won ! "
    return "You lost!"
def who_wins(player,op):
    if (player == 'r' and op =='s') or (player == 's' and op == 'p') or (player == 'p' and op == 'r'):
        return True
print(play())                