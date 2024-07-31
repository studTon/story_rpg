'''

Little story about a character

Made under MIT License by studTon

'''
import os
import time

# Function to create story

def story(name):
    """Function that writes chapter one of story."""
    os.system("clear")
    time.sleep(3.0)
    os.system("clear")
    print("""CHAPTER ONE""")
    print("""Everyone was happy in the kingdom of joy.""")
    print('''This kingdom was ruled by '''+ name + '''.''')
    time.sleep(7.0)
#########################


print("Hello world!")
os.system("clear")

character = input("Please, enter a name:")

f = open("male.txt", "r").readlines()

for name in f:
    name_processed = name.split()
    #print(name_processed[0])
    if str(name_processed[0]) == str(character):
        story(character)
        break;

