from random import choice
from game_data import data
from art import logo,vs
import os
#for clearing the terminal
def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS/Linux
    else:
        os.system('clear')
def choose(data,p_list=[]):
    if p_list==[]:
        return choice(data)
    y=choice(data)
    while y in p_list:
       y=choice(data)
    return y
p_list=[]
a=choose(data)
b=choose(data,[a])
score=0
p_list.extend([a,b])
is_game_over=False
while not is_game_over:
    clear_console()
    print(logo)
    if score!=0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    result=a["follower_count"]>b["follower_count"]
    if (guess=='a' and result) or (guess=='b' and not result):
        score+=1
        a=b
        b=choose(data,p_list)
    else:
        is_game_over=True
        clear_console()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    if len(p_list) == len(data):
        print(f"You win. Final score: {score}")
        break
    p_list.append(b)