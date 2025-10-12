import random
import os
import colorama


os.system("cls") if os.name == "nt" else os.system("clear")

easy = [
    'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Denmark', 'Egypt', 'France',
    'Germany', 'Greece', 'Indonesia', 'Israel', 'Italy', 'Japan', 'Mexico', 'Netherlands',
    'Norway', 'Philippines', 'Poland', 'Portugal', 'Russia', 'South Africa', 'South Korea',
    'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States',
    'Vietnam', 'Morocco', 'Saudi Arabia', 'Argentina'
]

normal = [
    'Austria', 'Bangladesh', 'Belgium', 'Bulgaria', 'Chile', 'Colombia', 'Croatia', 'Czechia',
    'Denmark', 'Finland', 'Georgia', 'Greece', 'Hungary', 'Ireland', 'Israel', 'Jordan',
    'Kazakhstan', 'Kenya', 'Malaysia', 'Morocco', 'Nepal', 'Netherlands', 'New Zealand',
    'Norway', 'Oman', 'Pakistan', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
    'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'Sri Lanka', 'Thailand', 'Turkey', 'Ukraine',
    'Uzbekistan', 'Vietnam', 'Argentina', 'Bangladesh', 'Croatia', 'Kazakhstan', 'Lebanon', 'Jordan',
    'Nepal', 'Oman', 'Serbia', 'Slovakia', 'Slovenia'
]

hard = [
    'Algeria', 'Andorra', 'Armenia', 'Azerbaijan', 'Bolivia', 'Bosnia and Herzegovina',
    'Cambodia', 'Central African Republic', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador',
    'Ghana', 'Honduras', 'Hungary', 'Iceland', 'Laos', 'Maldives', 'Mauritius', 'Mexico',
    'Moldova', 'Montenegro', 'Myanmar (Burma)', 'Namibia', 'North Macedonia', 'Panama',
    'Paraguay', 'Rwanda', 'South Sudan', 'Sudan', 'Tanzania', 'Trinidad and Tobago',
    'Uruguay', 'Zambia', 'Zimbabwe', 'Bangladesh', 'Botswana', 'Croatia', 'Jordan', 'Kazakhstan',
    'Kosovo', 'Nepal', 'Oman', 'Qatar', 'Romania', 'Serbia', 'Slovakia', 'Slovenia', 'Sri Lanka',
    'Ukraine', 'Uzbekistan', 'Laos', 'Cambodia', 'Papua New Guinea', 'Malawi', 'Mozambique',
    'Syria', 'Haiti', 'Iceland', 'Montenegro', 'Rwanda', 'Maldives', 'Namibia', 'Trinidad and Tobago'
]

expert = [
    'Bahamas', 'Bahrain', 'Barbados', 'Belize', 'Benin', 'Bhutan', 'Brunei', 'Burkina Faso',
    'Burundi', 'Cabo Verde', 'Cameroon', 'Comoros', 'Djibouti', 'Dominica', 'Equatorial Guinea',
    'Eswatini (Swaziland)', 'Fiji', 'Gabon', 'Gambia', 'Grenada', 'Guinea', 'Guinea-Bissau',
    'Guyana', 'Kiribati', 'Kyrgyzstan', 'Lesotho', 'Liberia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Micronesia', 'Monaco',
    'Nauru', 'North Korea', 'Palau', 'Palestine', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Senegal',
    'Seychelles', 'Sierra Leone', 'Solomon Islands', 'Somalia', 'Suriname', 'Tajikistan',
    'Timor-Leste', 'Togo', 'Tonga', 'Turkmenistan', 'Tuvalu', 'United Arab Emirates',
    'Vanuatu', 'Vatican City', 'Yemen', 'Central African Republic', 'Equatorial Guinea'
]



def show_game(goal, hinted_words):
        print(' '.join(goal[i] if hinted_words[i] else " _"for i in range(len(goal)) ))    

def points():
    with open("points.txt", 'r') as point_file:
        point = point_file.readline()
        return int(point)

def save_points(point):
    with open("points.txt", 'w') as point_file:
        point_file.write(str(point))



point = points()

q = True
number_of_faileds = 0


menu = f'''
{colorama.Fore.RED}1> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Start Game{colorama.Style.RESET_ALL}
            
{colorama.Fore.RED}2> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Difficulty Level{colorama.Style.RESET_ALL} 
             
{colorama.Fore.RED}3> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Quit{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}4> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Clear Screen{colorama.Style.RESET_ALL}              

{colorama.Fore.RED}5> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Score{colorama.Style.RESET_ALL}              

'''
diff_number = "2"
difficulty_level = {
                    "1": easy, 
                    "2": normal, 
                    "3": hard, 
                    "4": expert
                    }
while q:
    colorama.init(autoreset=True)
    goal = random.choice(difficulty_level[diff_number])
    print(menu)


    user_input = input(colorama.Fore.RED + "> ")
    print(colorama.Style.RESET_ALL)           

    match user_input:
        case "1":
            winning_condition = False
            os.system("cls") if os.name == "nt" else os.system("clear")
            hinted_words = [False for _ in range (len(goal)+1)]
            number_of_faileds = 0
            while (number_of_faileds) < len(goal)-1:
                hinted_words[0] = True     
                print(f"Difficulty: {diff_number}\n\n")           
                show_game(goal, hinted_words)
                user_input= input(colorama.Fore.RED +"\n> ")
                print(colorama.Style.RESET_ALL)           
                
                if user_input == goal or user_input == goal.lower():
                    os.system("cls") if os.name == "nt" else os.system("clear")
                    winning_condition = True
                    print(colorama.Back.RED + colorama.Fore.BLACK +  "Correct" + colorama.Style.RESET_ALL )
                    point += 1
                    break
                elif user_input == "3": 
                    q = False
                else:
                    number_of_faileds += 1
                    hinted_words[number_of_faileds] = True
            if not winning_condition:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print(colorama.Back.RED + colorama.Fore.BLACK + f"You Lost the answer is {goal}" + colorama.Style.RESET_ALL )
        case "2":
            diff_menu = f'''
{colorama.Fore.RED}1> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Easy{colorama.Style.RESET_ALL}
{colorama.Fore.RED}2> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Normal{colorama.Style.RESET_ALL}
{colorama.Fore.RED}3> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Hard{colorama.Style.RESET_ALL}
{colorama.Fore.RED}4> {colorama.Style.RESET_ALL}{colorama.Back.GREEN + colorama.Fore.BLACK}Expert{colorama.Style.RESET_ALL}
            '''
            os.system("cls") if os.name == "nt" else os.system("clear")
            print(diff_menu)
            diff_number = input("> ")
            os.system("cls") if os.name == "nt" else os.system("clear")
        case "3":
        
            q=False
            save_points(point)
        case "4":
            os.system("cls") if os.name == "nt" else "clear"
        case "5":
                    
                    print(f"**************** you earned {point} points today****************")
