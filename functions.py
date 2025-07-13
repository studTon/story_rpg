import os
import time
import pygame

character = "king name"


def game_menu(option):
    """Game menu options"""
    while option != 3: 
        if option == 1: #Play
            os.system("clear")
            character = input("Enter a male name: ")
            print("It's a story that begins a long time ago...")
            f = open("male.txt", "r").readlines()
            for name in f:
                name_processed = name.split()
                if str(name_processed[0]) == str(character):
                    True
                else:
                    break
            char_option = intro(character)
            chapter_one(char_option)
            return 10
        elif option == 2: #How to play?
            print("Under construction")
            break
        elif option == 3: #Exit
            break
        else:
            print("WRONG OPTION. Run again\n")
            break;

def start_game():
    pygame.mixer.init()
    ost = "alex-productions-medieval-and-celtic-music-lands.mp3"
    pygame.mixer.music.load(ost)
    pygame.mixer.music.play(0,0,1)
    """Function that initialize game"""
    art = """

        | |_| |_| |                 | |_| |_| |
        \  .      /                 \ .    .  /
        \    ,  /                   \    .  /
        | .   |_   _   _   _   _   _| ,   |
        |    .| |_| |_| |_| |_| |_| |  .  |
        | ,   | .    .     .      . |    .|	
        |.    | .    |+++++++| .    |   . |
        |   . |   ,  |+++++++|.  . _|__   |
     	------------------------------------
							
    """
    os.system("clear")
    print("Hello world!\n")
    input("Press Enter to continue...")
    os.system("clear")
    print("This adventure game is called:")
    time.sleep(3.0)
    os.system("clear")
    print("                ======= STORY RPG =======")
    print(art)
    input("Press Enter to continue...")
    os.system("clear")
    print("MAIN MENU\n1 - Play \n2 - How to Play? \n3 - Exit\n")
    menu_option = int(input("Enter a number from options above: "))
    game_menu(menu_option)


def intro(person):
    """Describe a brief story of the kingdom."""
    os.system("clear")
    input("Press Enter to continue...")
    os.system("clear")
    print("""INTRODUCTION""")
    print("""Everyone was happy in the Kingdom of Joy.""")
    print('''This kingdom was ruled by '''+ person + '''.''')
    print("The Kingdom of Joy was ruled with love and passion to serve other kingdoms.")
    print("The king was a noble man, and also his court and serfs.")
    input("Press Enter to continue...")
    print("King "+ person +" decided to invite his serfs to a great party.")
    print("It was a thanks giving party.")
    print("He choose his...")
    print("0 - Knight\n1 - Archer \n2 - Infantry \n3 - Crossbowman\n")
    rpg_character = int(input("Choose an option between 0 and 3: "));
    return rpg_character

def chapter_one(character):
    """Chapter one: The adventure begins"""
    match character: #create a option switch with return.
        case 0: print("The Knight with his strong power mounted his horse and received a mission.\n")
        
        case 1: print("The Archer with his longbow prepared his bag of arrows to defend from enemies.\n")

        case 2: print("The Infantry man followed his group of soldiers to defend the fortress.\n")

        case 3: print("The Crossbowman got his crossbow to attack the foes with his bolts.\n")
    input("Press Enter to continue...")

