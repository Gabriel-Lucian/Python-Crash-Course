"""
Extra whitespace can be confusing in your programs.
Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right end of a string, use
the rstrip() method.
"""
# printing with whitespace
favorite_language = "Pyton "
print(favorite_language)

# TEMPORARY - Avoiting to print the white space - Python can look for extra whitespace on the right and left sides of a
# string. To ensure that no whitespace exists at the right end of a string, use
# the rstrip() method.

favorite_language = "Pyton "
print(favorite_language.rstrip())


# PERMANENT ! - To remove the whitespace from the string permanently, you have to
# associate the stripped value with the variable name: rstrip() for right side / lstrip() for left side / and strip() for both sides!!!

favorite_language = "Pyton "
favorite_language = favorite_language.strip()
print(favorite_language)

