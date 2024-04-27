
from game_data import data
import random

from replit import clear

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'



def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return(f"{account_name}, a {account_descr} , from {account_country}")
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
        
        
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? type 'A' or 'B'").lower()

    a_follower_count = account_a["follower_count"]


    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score+=1
        print(f"You're right!, Current score: {score}")
    else:
        game_should_continue = False
        print(f"You're wrong, Final score: {score}")
        
        
        
