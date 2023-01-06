"""
Use a variable to represent a persons name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
"""
# Ask for the user name
name = input("Please tell me your name: ")
#Greetings the user! using the method .title() help us to capitalize the first letter in a name
# and the method .strip() help python to delete(strip) any extra whitespace in the end or biggining of the input!
print(f"Hello {name.lower().title().strip()}, would you like to learn some Python today?")