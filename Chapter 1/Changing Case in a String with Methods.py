"""
A string is a series of characters. Anything inside quotes is considered
a string in Python, and you can use single or double quotes around your
strings like this:
>>> "This is a string."
>>> 'This is also a string.'

 --- Changing Case in a String with Methods ---
One of the simplest tasks you can do with strings is change the case of the
words in a string. Look at the following code, and try to determine what’s
happening:
"""
name = "gabriel nechifor"

print(name.title())

"""
In this example, the variable name refers to the lowercase string "ada
lovelace". 
The method title() appears after the variable in the print() call.
A method is an action that Python can perform on a piece of data. The dot
(.) after name in name.title() tells Python to make the title() method act on
the variable name.
"""
name = "Gabriel Nechifor"

print(name.upper())
print(name.lower())

