'''Little story about a character'''

print("Hello world!")


list_of_names = open("male.txt").read()

'''Write here a code to compare male name.'''

character = input("Please, enter a name:")

def story(name):
    """Function that writes chapter one of story."""
    print("""CHAPTER ONE""")
    print("""Everyone was happy in the kingdom of joy.""")
    print('''This kingdom was ruled by '''+ name + '''.''')


story(character)