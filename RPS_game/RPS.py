import random
from re import S

def play():
    user=input(" Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer=random.choice(['r','p','s'])
    
    if user==computer:
        return 'tie'
    if is_win(user,computer):
        return 'You Won!'
    
    print(computer)
    return 'You lost </3 T_T :(('
    
def is_win(player,opponent):
    if (player== 'r' and opponent=='s') or(player=='s' and opponent=='p') or (player=='p'and opponent=='r'):
        return True
    

print(play())