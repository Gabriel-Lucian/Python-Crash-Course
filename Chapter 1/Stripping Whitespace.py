"""
Extra whitespace can be confusing in your programs.
Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right end of a string, use
the rstrip() method.
"""
# printing with whitespace
favorite_language = "Pyton "
print(favorite_language)

# Avoiting to print the white space - Python can look for extra whitespace on the right and left sides of a
# string. To ensure that no whitespace exists at the right end of a string, use
# the rstrip() method.

favorite_language = "Pyton "
print(favorite_language.rstrip())