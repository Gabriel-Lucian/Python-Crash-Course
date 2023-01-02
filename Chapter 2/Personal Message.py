"""
Use a variable to represent a persons name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
"""
name = input("Please tell me your name: ")

print(f"Hello {name.lower().title().strip()}, would you like to learn some Python today?")