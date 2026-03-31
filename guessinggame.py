# Set the target number that the player needs to guess
answer = 5

# Prompt the user to make their first guess
print("Please guess a number between 1 and 10: ")
# Convert the user's input from string to integer
guess = int(input())

# This variation eliminates the duplication of code found in the commented-out
# code below. It uses nested conditionals to avoid repeating the success/failure
# checks that were present in the original code.
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher.")
#     else:   # guess must be greater than answer
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time.")

# Current implementation: Check if the player guessed correctly on their first try
if guess == answer:
    print("You got it first time.")
else:
    # If the first guess was incorrect, provide feedback on direction
    if guess < answer:
        print("Please guess higher.")
    else:
        # guess must be greater than answer
        print("Please guess lower.")
    # Ask the player for a second guess
    guess = int(input())
    # Check if the second guess is correct
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")

# Original code - this code has a lot of duplication, which is not ideal.
# The same success/failure checks are repeated multiple times within each branch.
# This demonstrates why refactoring is important for code maintainability.
#
# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > answer:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time.")
