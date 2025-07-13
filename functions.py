import os
import pygame
import time

character = "king name"


def game_menu():
    """Game menu options"""
    playing = True
    while playing:
        os.system("clear")
        print("MAIN MENU\n1 - Play \n2 - How to Play? \n3 - Exit\n")
        option = int(input("Enter a number from options above: "))
        if option == 1: # Play game
            os.system("clear")
            king = input("Enter a male name: ")
            print("It's a story that begins a long time ago...")
            time.sleep(5.0)
            f = open("male.txt", "r").readlines()
            for name in f:
                name_processed = name.split()
                if str(name_processed[0]) == str(character):
                    break
            # Story functions interaction
            intro_option = intro(king)
            chapter_one(intro_option)
        elif option == 2: # How to play?
            os.system("clear")
            print("Game under construction.\n\n Story RPG is a role-playing-game where you create a story about a medieval quest to defend a kingdom.\n You will face decisions with consequences each time you see the story.")
            input("\n Press Enter to continue to main menu...")
        elif option == 3: # Exit
            os.system("clear")
            playing = False
        else: # Invalid option
            os.system("clear")
            print("WRONG OPTION. Run again\n")
            input("Press Enter to continue...")

def start_game():
    """Game brief introduction"""
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
    =============================================
    =============================================
							
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
    time.sleep(3.0)
    input("Press Enter to continue...")
    os.system("clear")
    game_menu()


def intro(name):
    """Describe a brief story of the kingdom."""
    os.system("clear")
    input("Press Enter to continue...")
    os.system("clear")
    print("\n")
    print("""INTRODUCTION""")
    print("\n")
    print("""Everyone was happy in the Kingdom of Joy.""")
    print('''This kingdom was ruled by '''+ name + '''.''')
    print("The Kingdom of Joy was ruled with love and passion to serve other kingdoms.")
    print("The king was a noble man, and also his court and serfs.")
    input("Press Enter to continue...")
    os.system("clear")
    print("King "+ name +" decided to invite his serfs to a great party.")
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

