import os
import time

def start_app():
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
						
				PRESS Q to continue	
    """
    os.system("clear")
    print("Hello world!")
    time.sleep(3.0)
    os.system("clear")
    print("This adventure is called:")
    time.sleep(3.0)
    os.system("clear")
    print("======= STORY RPG =======")
    print(art)
    ost = "alex-productions-medieval-and-celtic-music-lands.mp3"
    os.system("mpg123 -q -o alsa " + ost)
    time.sleep(8.0)
    os.system("clear")

def story(person):
    """Function that describe the main story."""
    os.system("clear")
    time.sleep(3.0)
    os.system("clear")
    print("""INTRODUCTION""")
    print("""Everyone was happy in the kingdom of joy.""")
    print('''This kingdom was ruled by '''+ person + '''.''')
    print("The kingdom of joy was ruled with love and passion to serve other kingdoms.")
    print("The king was a noble man, and also his court and serfs.")
    time.sleep(10.0)
    print("King "+ person +" decided to invite his serfs to a great party.")
    print("It was a thanks giving party.")
    print("He choose his...")
    #create a option switch with return.

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
