import os
import pygame
import re
import time

character = "king name"
ost1 = "ost/Majestic Hills.mp3"
ost2 = "ost/alex-productions-medieval-and-celtic-music-lands.mp3"
ost3 = "ost/Heroic Age.mp3"
art = """

          |-|__|-|            |-|__|-|
          |      |            |      |
          |      |            |      |
          | ------------------------ |
          | ________________________ |
          ||                        ||
          ||          ___           ||
          ||         |   |          ||
          ||         |   |          ||
==================================================

"""

def start_game():
    """Game startup"""
    pygame.mixer.init()
    pygame.mixer.music.load(ost1)
    pygame.mixer.music.play(0,0,1)
    os.system("clear")
    print("Hello world!\n")
    input("Press Enter to continue...")
    os.system("clear")
    print("This adventure game is called:")
    time.sleep(1.5)
    os.system("clear")
    print("            ======= STORY RPG =======")
    print(art)
    time.sleep(3.0)
    input("Press Enter to continue...")
    os.system("clear")
    game_menu()

def game_menu():
    """Game menu options"""
    playing = True
    while playing:
        pygame.mixer.music.load(ost2)
        pygame.mixer.music.play(0,0,1)
        os.system("clear")
        print("MAIN MENU\n1 - Play \n2 - How to Play? \n3 - Credits\n4 - Exit\n")
        option = int(input("Enter a number from options above: "))
        if option == 1: # Play game
            os.system("clear")
            pygame.mixer.stop()
            pygame.mixer.music.load(ost3)
            pygame.mixer.music.play(0,0,1)
            king = define_king()
            manage_story(king)
        elif option == 2: # How to play?
            os.system("clear")
            print("Game under construction.\n\n Story RPG is a role-playing-game where you create a story about a medieval quest to defend a kingdom.\n You will face decisions with consequences each time you see the story.\n All the gameplay is made on command-line interface.")
            input("\n Press Enter to continue to main menu...")
        elif option == 3: # Game credits
            os.system("clear")
            print("Design: studTon\nSoundtrack by: Alex-Productions & Kevin MacLeod\nGame story: studTon")
            input("\n Press Enter to continue to main menu...")
        elif option == 4: # Exit
            os.system("clear")
            playing = False
        else: # Invalid option
            os.system("clear")
            print("WRONG OPTION. Run again\n")
            input("Press Enter to continue...")

def define_king():
    """Write a name for the king"""
    print("It's a story that begins a long time ago...")
    time.sleep(2.5)
    check = False
    while check == False:
        os.system("clear")
        king = input("Enter a valid name for the king.\nKing's name: ")
        match = re.search(r'^(?:[A-Z][a-z]+[-\s]?)+$', king)
        # If-statement after search() tests if it succeeded
        if match:
            check = True
            return king 
        else:
            print('Input a valid name.')
            time.sleep(2.5)

def manage_story(king_name):
    """Manage interaction between chapters"""
    intro_option = intro(king_name)
    choice_one = chapter_one(intro_option)
    choice_three = chapter_two(choice_one)

def intro(name):
    """Intro: Describe a brief story of the kingdom."""
    os.system("clear")
    print("\n")
    print("""INTRODUCTION""")
    print("\n")
    print("""Everyone was happy in the Kingdom of Joy.""")
    print('''This kingdom was ruled by '''+ name + '''.''')
    print("The Kingdom of Joy was ruled with love and passion to serve other kingdoms.")
    print("The king was a noble man, and also his court and serfs.")
    input("Press Enter to continue...")
    selecting = False
    while selecting == False:
        os.system("clear")
        print("King "+ name +" decided to invite his serfs to a great party.")
        print("It was a thanks giving party.")
        print("He choose his...")
        print("0 - Knight\n1 - Archer \n2 - Infantry \n3 - Crossbowman\n")
        rpg_character = int(input("Choose an option between 0 and 3: "));
        print("")
        if rpg_character >= 0 and rpg_character <= 3:
            selecting = True
        else:
            print("Select a valid option.\n")
            input("Press Enter to continue...")
    os.system("clear")
    print("King " + name + " was really proud of his soldiers, because they serve him with honor.\n")
    print("He asked: \"My noble serf, we will face an attack suddenly, please could you help me with this mission?\"")
    match rpg_character:
        case 0:
            print("The Knight said: \"Of course, my liege. You can trust me for this mission.\"")
            input("Press Enter to continue...")
        case 1:
            print("The Archer said: \"Of course, my liege. You can trust me for this mission.\"")
            input("Press Enter to continue...")
        case 2:
            print("The Infantry said: \"Of course, my liege. You can trust me for this mission.\"")
            input("Press Enter to continue...")
        case 3:
            print("The Crossbowman said: \"Of course, my liege. You can trust me for this mission.\"")
            input("Press Enter to continue...")
    return rpg_character

def chapter_one(character):
    """Chapter one: The adventure begins"""
    os.system("clear")
    print("""CHAPTER ONE""")
    print("")
    match character:
        case 0: 
            print("The Knight with his strong power mounted his horse and received his mission.\n")
            print("He took the mission with joy, and is brave enough to face the enemy of the kingdom without mercy.\n")
            input("Press Enter to continue...")
            return 0
        
        case 1: 
            print("The Archer with his longbow prepared his bag of arrows to defend the kingdom from enemies.\n")
            print("He get prepared on the top of the tower. Over there he can fire the enemy with advantage.\n")
            input("Press Enter to continue...")
            return 1

        case 2: 
            print("The Infantry man followed his group of soldiers to defend the fortress.\n")
            print("The infantry group get prepared to fight behind the walls of the fortress.\n")
            print("They scream with a loud voice: LONG LIVE THE KINGDOM!\n")
            input("Press Enter to continue...")
            return 2

        case 3: 
            print("The Crossbowman got his crossbow to attack the foes with his bolts.\n")
            print("Every time he saw a strange movement on the forest nearby, the bow could take an accuracy shot.\n")
            input("Press Enter to continue...")
            return 3

    print("The enemy general said with loud voice: \"The kingdom of Numberland has one thing to say to you all. Please, avoid any conflict.\"\n")
    print("\"It's easy to you surrender to our great army or you will gonna face the siege. Think wisely, I recommend...\"\n")
    input("Press Enter to continue...")
def chapter_two(choice):
    """Chapter two: The enemy arrives to siege the fortress."""
    os.system("clear")
    print("""CHAPTER TWO""")
    print("The sunset was on the horizon and we could see the wind over the trees.\n")
    print("Suddenly, three army bands arrived on the top of a hill. They play a trumpet to announces the fight.\n")
    print("")
    input("Press Enter to continue...")
