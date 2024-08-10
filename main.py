'''

Little rpg story about a character

Made under MIT License by studTon

'''

from functions import *

start_app()

character = input("Please, enter a name:")

f = open("male.txt", "r").readlines()

for name in f:
    name_processed = name.split()
    if str(name_processed[0]) == str(character):
        story(character)
        break;
