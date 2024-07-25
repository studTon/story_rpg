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
os.system("clear")

character = input("Please, enter a name:")

f = open("male.txt", "r")

for name in f:
	if str(name) == str(character):
		story(character)
		break
	else:
		print("NAME UNFOUND")

