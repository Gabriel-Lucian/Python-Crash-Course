"""
Integers

You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

>>> 2 + 3 Addition
5

>>> 3 - 2 Substitution
1

>>> 2 * 3 Multiplication
6

>>> 3 / 2 Simplification
1.5

>>3**2 to the power of
9


Python supports the order of operations too, so you can use multiple
operations in one expression. You can also use parentheses to modify the
order of operations so Python can evaluate your expression in the order
you specify. For example:

>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
"""

"""
Floats
Python calls any number with a decimal point a float. This term is used
in most programming languages, and it refers to the fact that a decimal
point can appear at any position in a number.

>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
"""

"""
Integers and Floats
When you divide any two numbers, even if they are integers that result in a
whole number, youll always get a float:
>>> 4/2
2.0
If you mix an integer and a float in any other operation, youll get a
float as well:
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
Python defaults to a float in any operation that uses a float, even if the
output is a whole number.
"""

"""
Underscores in Numbers: !!!
When you’re writing long numbers, you can group digits using underscores
to make large numbers more readable:

universe_age = 14_000_000_000
print(universe_age)

When you print a number that was defined using underscores, Python
prints only the digits:
>>> print(universe_age)

14000000000

Python ignores the underscores when storing these kinds of values.
Even
if you dont group the digits in threes, the value will still be unaffected.
To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature
works for integers and floats, but its only available in Python 3.6
and later.


universe_age = 14_000_000_000
print(universe_age)
"""
"""
Multiple Assignment: !!!

You can assign values to more than one variable using just a single line.
This can help shorten your programs and make them easier to read; you’ll
use this technique most often when initializing a set of numbers.
For example, here’s how you can initialize the variables x, y, and z
to zero:
>>> x, y, z = 0, 0, 0
You need to separate the variable names with commas, and do the
same with the values, and Python will assign each value to its respectively
positioned variable. As long as the number of values matches the number of
variables, Python will match them up correctly.

x, y, z = 0, 0, 0
"""

"""
Constants !!!
A constant is like a variable whose value stays the same throughout the life
of a program. Python doesnt have built-in
constant types, but Python programmers
use all capital letters to indicate a variable should be treated as a
constant and never be changed:
MAX_CONNECTIONS = 5000
When you want to treat a variable as a constant in your code, make the
name of the variable all capital letters.
"""