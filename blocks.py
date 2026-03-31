# This script prompts the user for their name and age,
# then determines if they are old enough to vote,
# with a special case for age 900 (Yoda reference).

# Prompt the user to enter their name
name = input("Please enter your name: ")

# Prompt the user to enter their age, using their name in the message
age = int(input("How old are you, {0}? ".format(name)))

# Print the entered age
print(age)

# Check if the user is under 18
if age < 18:
    print("Please come back in {0} years.".format(18 - age))
# Special case for age 900, referencing Yoda from Star Wars
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
# If 18 or older (and not 900)
else:
    print("You are old enough to vote.")
    print("Please put an X in the box.")
