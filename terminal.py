from math import floor
import os
import random

import climage
import colorama
from pyfiglet import figlet_format

from data import all_countries, easy, expert, flags_map, hard, normal


def show_game(goal, hinted_words):
    goal_flag = climage.convert(f"flags/{flags_map[goal]}", is_unicode=True, is_256color = True    , width= 25)
    print(goal_flag, "\n")
    print(' '.join(goal[i] if hinted_words[i] else " _"for i in range(len(goal))))    

def points():
    with open("points.txt", 'r') as point_file:
        point = point_file.readline()
        return int(point)

def save_points(point):
    with open("points.txt", 'w') as point_file:
        point_file.write(str(point))
def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")
def reset_points():
    open("points.txt", "w").close()
    with open("points.txt", "w") as f:
        f.write("0")
def banner(win_con):
    if win_con:
        print(colorama.Back.RED + colorama.Fore.BLACK +  "Correct" + colorama.Style.RESET_ALL )  # ty: ignore[unsupported-operator]
        
    elif not win_con:
        print(colorama.Back.RED + colorama.Fore.BLACK + f"You Lost the answer is {old_goal}" + colorama.Style.RESET_ALL )  # ty: ignore[unsupported-operator]
    else:
        pass

############################################################################
clear_screen()
reset_points()
point = points()
q = True
number_of_faileds = 0
points_show = False
menu = f'''
{colorama.Fore.RED}1 > {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Start Game{colorama.Style.RESET_ALL}
                         
{colorama.Fore.RED}2 > {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Score{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}C > {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Clear Screen{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}Q > {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Quit{colorama.Style.RESET_ALL}              

'''
difficulty_level = {
                    "easy": 1, 
                    "normal": 2, 
                    "hard": 3, 
                    "expert": 4
                    }
while True:
    colorama.init(autoreset=True)
    print(figlet_format("CONGUESS", font="slant"))
    if points_show:
        points_show = False
        print(f"**************** you earned {point} points today****************")
    print(menu)


    user_input = input(colorama.Fore.RED + "> ").strip()  # ty: ignore[unsupported-operator]
    print(colorama.Style.RESET_ALL)           

    match user_input:
        case "1":
            winning_condition = "start"
            while user_input != "5":
                goal = random.choice(all_countries)
                if goal in easy:
                    diff_num = "easy"
                elif goal in normal:
                    diff_num = "normal"
                elif goal in hard:
                    diff_num = "hard"
                elif goal in expert:
                    diff_num = 'expert' 
                clear_screen()

                hinted_words = [False for _ in range (len(goal)+1)]
                number_of_faileds = 0
                banner(winning_condition)
                while (number_of_faileds) < floor(len(goal)*0.8):
                    hinted_words[0] = True     
                    print(f"Difficulty: {difficulty_level[diff_num]}\n\n")           
                    show_game(goal, hinted_words)
                    user_input= input(colorama.Fore.RED +"\n> ").strip()  # ty: ignore[unsupported-operator]
                    print(colorama.Style.RESET_ALL)
                    clear_screen()
                    if user_input == goal or user_input == goal.lower():
                        clear_screen()
                        winning_condition = True
                        point += difficulty_level[diff_num]
                        break
                    elif user_input == "5": 
                        winning_condition = "start"
                        clear_screen()
                        break
                    else:
                        winning_condition = False
                        number_of_faileds += 1
                        hinted_words[number_of_faileds] = True
                old_goal = goal
                banner(winning_condition)

        case "2":
            points_show = True
            clear_screen()
        case "c":
            clear_screen()

        case "q":
            break
        case _:
            clear_screen()






r"""
  ____ _  _  ____  _   _ 
 / ___| || |/ ___|| | | |
| |  _| || |\___ \| |_| |
| |_| |__   _|__) |  _  |
 \____|  |_||____/|_| |_|
"""
