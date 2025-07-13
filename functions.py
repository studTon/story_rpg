import os
import time
import pygame

def start_app():
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
    print("Hello world!")
    time.sleep(3.0)
    os.system("clear")
    print("This adventure is called:")
    time.sleep(3.0)
    os.system("clear")
    print("                ======= STORY RPG =======")
    print(art)
    time.sleep(8.0)
    os.system("clear")

def story(person):
    """Function that describe the main story."""
    os.system("clear")
    time.sleep(3.0)
    os.system("clear")
    print("""INTRODUCTION""")
    print("""Everyone was happy in the Kingdom of Joy.""")
    print('''This kingdom was ruled by '''+ person + '''.''')
    print("The Kingdom of Joy was ruled with love and passion to serve other kingdoms.")
    print("The king was a noble man, and also his court and serfs.")
    time.sleep(10.0)
    print("King "+ person +" decided to invite his serfs to a great party.")
    print("It was a thanks giving party.")
    print("He choose his...")
    print("0 - Knight\n1 - Archer \n2 - Infantry \n3 - Crossbowman\n")
    rpg_character = int(input("Choose an option between 0 and 3: "));
    return rpg_character

def chapter_one(character):
    """Chapter one: The adventure begins"""
    match character: #create a option switch with return.
        case 0: print("The Knight with his strong power mounted his horse and received a mission.")
        
        case 1: print("The Archer with his longbow prepared his bag of arrows to defend from enemies.")

        case 2: print("The Infantry man followed his group of soldiers to defend the fortress.")

        case 3: print("The Crossbowman got his crossbow to attack the foes with his bolts.")
    input("Press Enter to continue...")

def game_start(option):
    while option != 3: 
        if option == 1: #Play
            os.system("clear")
            print("It's a story that begins a long time ago...")
            time.sleep(3.0)
            return 10
        elif option == 2: #Settings
            print("Under construction")
        elif option == 3: #Exit
            break
        else:
            print("WRONG OPTION.")
