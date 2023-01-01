"""
In some situations, you’ll want to use a variable’s value inside a string. For
example, you might want two variables to represent a first name and a last
name respectively, and then want to combine those values to display someone’s
full name:
"""
# # Ask for name from the user
# name = input("Please tell me your name: ")
# # Ask for surname from the user
# surname = input("Please tell me your surname: ")
# # Transform the name and surname in lower cases if the user will input upper caps, 
# # and transform the first caps in upper caps
# name = name.lower().title()
# surname = surname.lower().title()
# # Use variables in string
# full_name = f"{name} {surname}"

# print(full_name)

# OR BETTER

# # Ask for name and surname
# name = input("Please tell me your name: ")  

# surname = input("Please tell me your surname: ")

# # Use the variables in a string, and avoid a problem if the user will input upper cases, so 
# # we have to add lower(), and title() to do the cases lower, and to do the first case upper!
# full_name = f"{name} {surname}"
# message = f"Hello, {full_name.lower().title()}!"
# print(message)



