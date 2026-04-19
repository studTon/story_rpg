"""Functions used inside the gameplay."""

import os
import random
import re
import sys
import time

import pygame

import config


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller external assets."""
    if getattr(sys, "frozen", False):
        # Path to the directory where the binary executable is located
        base_path = os.path.dirname(sys.executable)
    else:
        # Path to the directory where the script is located
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def clear_screen():
    """Clears the console screen based on OS."""
    os.system("cls" if os.name == "nt" else "clear")


def set_console_size(width=80, height=30):
    """Sets the console size."""
    if os.name == "nt":
        os.system(f"mode con: cols={width} lines={height}")
    else:
        sys.stdout.write(f"\x1b[8;{height};{width}t")


def play_music(track, loops=0, start=0.0, fade_ms=0):
    """Load and play a music track."""
    try:
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(loops, start, fade_ms)
    except Exception as e:
        print(f"Error playing music: {e}")


def play_sound(track):
    """Load and play a sound effect."""
    if track == SFX3:
        pygame.mixer.music.stop()
    try:
        sound = pygame.mixer.Sound(track)
        sound.play()
    except Exception as e:
        print(f"Error playing sound: {e}")


def slow_print(text, delay=0.03):
    """Print text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Print a newline at the end


def start_game():
    """Game startup"""
    pygame.mixer.init()

    # Set the Window Icon
    try:
        icon_img = pygame.image.load(resource_path(ICON))
        pygame.display.set_icon(icon_img)
    except Exception:
        pass

    play_music(OST1)
    clear_screen()
    slow_print("Hello world!\n")
    input("Press Enter to continue...")
    clear_screen()
    slow_print("This adventure game is called:")
    time.sleep(1.5)
    clear_screen()
    print("            ======= STORY RPG =======")
    print(ART)
    time.sleep(3.0)
    input("Press Enter to continue...")
    clear_screen()
    game_menu()


def game_menu():
    """Game menu options"""
    playing = True
    while playing:
        play_music(OST2)
        clear_screen()
        print(
            "MAIN MENU\n=======*=======*=======\n1 - Play \n2 - How to Play? \n3 - Credits\n4 - Exit\n"
        )
        option = int(input("Enter a number from options above: "))
        if option == 1:  # Play game
            clear_screen()
            clear_screen()
            pygame.mixer.music.stop()
            play_music(OST3)
            king = define_king()
            manage_story(king)
        elif option == 2:  # How to play?
            clear_screen()
            print(
                "Game under construction.\n\n Story RPG is a role-playing-game where you create a story about a medieval quest to defend a kingdom.\n You will face decisions with consequences each time you see chapters rolling.\n All the gameplay is on command-line interface.\nFeel free to enjoy each character interaction with the scenario you will face."
            )
            input("\n Press Enter to continue to main menu...")
        elif option == 3:  # Game credits
            clear_screen()
            print(
                "Design: studTon\nSoundtrack by: Alex-Productions, Kevin MacLeod, mokasza & Freesound\nGame story: studTon"
            )
            input("\n Press Enter to continue to main menu...")
        elif option == 4:  # Exit
            clear_screen()
            playing = False
        else:  # Invalid option
            clear_screen()
            print("WRONG OPTION. Run again\n")
            input("Press Enter to continue...")


def define_king():
    """Write a name for the king"""
    slow_print("It's a story that begins a long time ago...")
    time.sleep(2.5)
    check = False
    while check is False:
        clear_screen()
        king = input("Enter a valid name for the king.\nKing's name: ")
        match = re.search(r"^(?:[A-Z][a-z]+[-\s]?)+$", king)
        # If-statement after search() tests if it succeeded
        if match:
            check = True
            return king
        else:
            slow_print("Input a valid name.")
            time.sleep(2.5)


def manage_story(king_name):
    """Manage interaction between chapters"""
    total_accumulated_score = 0
    intro_option = intro(king_name)
    success, score, character = chapter_one(intro_option)
    if success:
        total_accumulated_score += score
        clear_screen()
        slow_print(f"Your total score now is: {total_accumulated_score} points\n")
        slow_print("Congratulations!\n")
        input("Press Enter to continue...")
        clear_screen()
        success, score, character = chapter_two(character)
        if success:
            total_accumulated_score += score
            clear_screen()
            slow_print(
                f"You have won with a total of {total_accumulated_score} points\n"
            )
            slow_print("You're in lucky!\n")
            input("Press Enter to continue...")
    else:
        clear_screen()
        slow_print(f"You have made {total_accumulated_score} points.\n")
        slow_print("But you lose.\n")
        game_over()


def intro(name):
    """Intro: Describe a brief story of the kingdom."""
    clear_screen()
    slow_print("\n")
    slow_print("""INTRODUCTION""")
    slow_print("\n")
    slow_print("""Everyone was happy in the Kingdom of Joy.""")
    slow_print(f"This kingdom was ruled by {name}.")
    slow_print(
        "The Kingdom of Joy was ruled with love and passion to serve other kingdoms."
    )
    slow_print("The king was a noble man, and also his court and serfs.")
    input("Press Enter to continue...")
    selecting = False
    while selecting == False:
        clear_screen()
        slow_print(f"King {name} decided to invite his serfs to a great party.")
        slow_print("It was a thanks giving party.")
        slow_print("He choose his...")
        slow_print("0 - Knight\n1 - Archer \n2 - Infantry \n3 - Crossbowman\n")
        rpg_character = int(input("Choose an option between 0 and 3: "))
        slow_print("")
        if rpg_character >= 0 and rpg_character <= 3:
            selecting = True
        else:
            slow_print("Select a valid option.\n")
            input("Press Enter to continue...")
    clear_screen()
    slow_print(
        f"King {name} was really proud of his soldiers, because they serve him with honor.\n"
    )
    slow_print(
        'He asked: "My noble serf, we will face an attack suddenly, please could you help me with this mission?"'
    )
    match rpg_character:
        case 0:
            slow_print(
                'The Knight said: "Of course, my liege. You can trust me for this mission."'
            )
            input("Press Enter to continue...")
        case 1:
            slow_print(
                'The Archer said: "Of course, my liege. You can trust me for this mission."'
            )
            input("Press Enter to continue...")
        case 2:
            slow_print(
                'The Infantry said: "Of course, my liege. You can trust me for this mission."'
            )
            input("Press Enter to continue...")
        case 3:
            slow_print(
                'The Crossbowman said: "Of course, my liege. You can trust me for this mission."'
            )
            input("Press Enter to continue...")
    return rpg_character


def chapter_one(character):
    """Chapter one: The adventure begins"""
    play_sound(SFX3)
    clear_screen()
    slow_print("""CHAPTER ONE""")
    slow_print("")
    match character:
        case 0:
            character = "knight"
            slow_print(
                "The Knight with his strong power mounted his horse and received his mission.\n"
            )
            slow_print(
                "He took the mission with joy, and is brave enough to face the enemy of the kingdom without mercy.\n"
            )
            input("Press Enter to continue...")

        case 1:
            character = "archer"
            slow_print(
                "The Archer with his longbow prepared his bag of arrows to defend the kingdom from enemies.\n"
            )
            slow_print(
                "He get prepared on the top of the tower. Over there he can fire the enemy with advantage.\n"
            )
            input("Press Enter to continue...")

        case 2:
            character = "infantry"
            slow_print(
                "The Infantry man followed his group of soldiers to defend the fortress.\n"
            )
            slow_print(
                "The infantry group get prepared to fight behind the walls of the fortress.\n"
            )
            slow_print("They scream with a loud voice: LONG LIVE THE KINGDOM!\n")
            input("Press Enter to continue...")

        case 3:
            character = "crossbowman"
            slow_print(
                "The Crossbowman got his crossbow to attack the foes with his bolts.\n"
            )
            slow_print(
                "Every time he saw a strange movement on the forest nearby, the bow can be used for an accurated shot.\n"
            )
            input("Press Enter to continue...")

    clear_screen()
    slow_print(
        'The enemy general said with loud voice: "The kingdom of Numberland has one thing to say to you all. Please, avoid any conflict."\n'
    )
    slow_print(
        '"It\'s easy to you surrender to our great army. Will you gonna face the siege? Think wisely, I recommend..."\n'
    )

    slow_print(f"Immediately, the {character} chose to?\n")
    print("0 - Stay on the tower (Low Risk)\n")
    print("1 - Hide in the forest (Medium Risk)\n")
    print("2 - Fight the enemy on open field (High Risk)\n")

    decision = int(input("Choose an option between 0 and 2: "))

    # Generate Stats
    luck = random.randint(1, 5)
    roll = random.randint(1, 10)
    total_score = roll + luck

    # Set Difficulty based on choice
    if decision == 0:
        difficulty = 8
    elif decision == 1:
        difficulty = 10
    else:
        difficulty = 12

    # Show Results
    slow_print(f"\n[BATTLE] Difficulty: {difficulty}")
    slow_print(f"[BATTLE] You rolled: {roll} + {luck} (Luck) = {total_score}")

    # Determine Outcome

    if total_score >= difficulty:
        play_sound(SFX2)
        slow_print(
            "VICTORY! Your strategy was successful. And you get some time to go back to the castle."
        )
        result = True
    else:
        play_sound(SFX1)
        slow_print("DEFEAT... The enemy overwhelmed you.")
        result = False

    input("Press Enter to continue...")
    pygame.mixer.stop()
    return result, total_score, character


def chapter_two(character):
    """Chapter two: The enemy arrives to siege the fortress."""
    play_music(OST3)
    clear_screen()
    slow_print("""CHAPTER TWO""")
    slow_print(
        "The sunset was on the horizon and we could see the wind over the trees.\n"
    )
    slow_print(
        "Suddenly, three army bands arrived on the top of a hill. They play a trumpet to announces the fight.\n"
    )
    slow_print(
        '"The Kingdom of Numberland shall never surrender to your fortress and your garrison troops.\n'
    )
    slow_print("Surrender or DIE!\n")
    input("Press Enter to continue...")
    clear_screen()
    slow_print(f"The {character} begin to assault into: \n")

    print("0 - Siege units (Low Risk)\n")
    print("1 - Archers (Medium Risk)\n")
    print("2 - Cavalry (High Risk)\n")

    decision = int(input("Choose an option between 0 and 2: "))

    # Generate Stats
    luck = random.randint(1, 5)
    roll = random.randint(1, 10)
    total_score = roll + luck

    # Set Difficulty based on choice
    if decision == 0:
        difficulty = 7
    elif decision == 1:
        difficulty = 10
    else:
        difficulty = 14

    # Show Results
    slow_print(f"\n[BATTLE] Difficulty: {difficulty}")
    slow_print(f"[BATTLE] You rolled: {roll} + {luck} (Luck) = {total_score}")

    if total_score >= difficulty:
        play_sound(SFX2)
        slow_print(
            "VICTORY! Your strategy was successful. And you get some time to go back to the castle."
        )
        result = True
    else:
        play_sound(SFX1)
        slow_print("DEFEAT... The enemy overwhelmed you.")
        result = False

    input("Press Enter to continue...")
    pygame.mixer.stop()
    return result, total_score, character


def game_over():
    """End the game"""
    clear_screen()
    slow_print("GAME OVER...")
    input("Press Enter to continue...")
