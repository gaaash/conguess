import random
import os
import colorama
from data import easy, normal, hard, expert
from pyfiglet import figlet_format
import emoji


def show_game(goal, hinted_words):
        print(' '.join(goal[i] if hinted_words[i] else " _"for i in range(len(goal)) ) + "\t"+ f"{emoji.emojize(f":{goal}:")}")    

def points():
    with open("points.txt", 'r') as point_file:
        point = point_file.readline()
        return int(point)

def save_points(point):
    with open("points.txt", 'w') as point_file:
        point_file.write(str(point))
def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")
############################################################################
clear_screen()

point = points()
q = True
number_of_faileds = 0
menu = f'''
{colorama.Fore.RED}1> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Start Game{colorama.Style.RESET_ALL}
            
{colorama.Fore.RED}2> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Difficulty Level{colorama.Style.RESET_ALL} 
             
{colorama.Fore.RED}3> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Score{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}4> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Clear Screen{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}5> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Quit{colorama.Style.RESET_ALL}              

'''

diff_num = "2"   #   default difficulty level
difficulty_level = {
                    "1": easy, 
                    "2": normal, 
                    "3": hard, 
                    "4": expert
                    }
while True:
    colorama.init(autoreset=True)
    goal = random.choice(difficulty_level[diff_num])
    print(figlet_format("CONGUESS", font="slant"))
    print(menu)


    user_input = input(colorama.Fore.RED + "> ").strip()
    print(colorama.Style.RESET_ALL)           

    match user_input:
        case "1":
            winning_condition = False
            clear_screen()
            hinted_words = [False for _ in range (len(goal)+1)]
            number_of_faileds = 0
            while (number_of_faileds) < len(goal)-1:
                hinted_words[0] = True     
                print(f"Difficulty: {diff_num}\n\n")           
                show_game(goal, hinted_words)
                user_input= input(colorama.Fore.RED +"\n> ").strip()
                print(colorama.Style.RESET_ALL)           
                
                if user_input == goal or user_input == goal.lower():
                    clear_screen()
                    winning_condition = True
                    print(colorama.Back.RED + colorama.Fore.BLACK +  "Correct" + colorama.Style.RESET_ALL )
                    point += 1
                    break
                elif user_input == "3": 
                    winning_condition = True
                    clear_screen()
                    break
                else:
                    number_of_faileds += 1
                    hinted_words[number_of_faileds] = True
            if not winning_condition:
                clear_screen()
                print(colorama.Back.RED + colorama.Fore.BLACK + f"You Lost the answer is {goal}" + colorama.Style.RESET_ALL )
        case "2":
            diff_menu = f'''
{colorama.Fore.RED}1> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Easy{colorama.Style.RESET_ALL}
{colorama.Fore.RED}2> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Normal{colorama.Style.RESET_ALL}
{colorama.Fore.RED}3> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Hard{colorama.Style.RESET_ALL}
{colorama.Fore.RED}4> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Expert{colorama.Style.RESET_ALL}
            '''
            clear_screen()
            print(diff_menu)
            diff_number = input("> ").strip()
            clear_screen()
        case "3":
            print(f"**************** you earned {point} points today****************")

        case "4":
            os.system("cls") if os.name == "nt" else "clear"
        
        case "5":
            break
            save_points(point)