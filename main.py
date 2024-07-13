'''Little story about a character'''
import os
import time

# Function to create story

def story(name):
    """Function that writes chapter one of story."""
    time.sleep(10.0)
    os.system("clear")
    print("""CHAPTER ONE""")
    print("""Everyone was happy in the kingdom of joy.""")
    print('''This kingdom was ruled by '''+ name + '''.''')

#########################


print("Hello world!")

with open("male.txt") as file:
    tuple_of_names = [tuple(line.split()) for line in file]

character = input("Please, enter a name:")

i = 0
while i < len(tuple_of_names):
    if character == tuple_of_names[i]:
        print("NAME FOUND!")
        story(character)
        break
    else:
        i += 1
