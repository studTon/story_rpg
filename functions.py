import os
import time

def start_app():
    """Function that initialize game"""
    print("Hello world!")
    time.sleep(3.0)
    os.system("clear")
    print("This is the adventure of:")
    time.sleep(3.0)
    os.system("clear")
    print("======= STORY RPG =======")
    time.sleep(8.0)
    os.system("clear")

def story(person):
    """Function that writes chapter one of story."""
    os.system("clear")
    time.sleep(3.0)
    os.system("clear")
    print("""CHAPTER ONE""")
    print("""Everyone was happy in the kingdom of joy.""")
    print('''This kingdom was ruled by '''+ person + '''.''')
    time.sleep(7.0)

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
