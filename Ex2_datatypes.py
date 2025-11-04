# -------------------------------------------
# Exercise 2: Commenting and Code Explanation
# -------------------------------------------
# In this exercise, you’ll practise how to:
# - Write clear, meaningful comments in Python
# - Explain what code does and why it’s written that way
# - Improve readability for anyone reading your programme
#
# You may discuss and work with your classmates,
# but each learner must submit their own file individually.
# -------------------------------------------


# Task 1: Basic Input and Output
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Basic Input and Output\n"
    + "-------------------------------------------")
# TODO:
# The code below asks for a user’s name and age, then prints a message.
# Your job: Add comments explaining what each line does.
# Write your comments using "#" on new lines or at the end of code lines.
#
# Example comment:
# # This line asks the user to type their name

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_datatypes.py
#    git commit -m "Completed task 1"
#    git push origin main
# -------------------------------------------



# Task 2: Working with Conditions
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Working with Conditions\n"
    + "-------------------------------------------")
# TODO:
# Add comments explaining what each part of the code does.
# Try to explain why the conditions are written this way.

temperature = float(input("Enter the current temperature in °C: "))

if temperature > 30:
    print("It's a hot day! Stay hydrated.")
elif temperature >= 15:
    print("Nice weather outside!")
else:
    print("It’s a bit chilly, wear something warm.")



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_datatypes.py
#    git commit -m "Completed task 2"
#    git push origin main
# -------------------------------------------



# Task 3: Loops and Lists
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Loops and Lists\n"
    + "-------------------------------------------")
# TODO:
# Add comments explaining what each line does.
# Hint: Think about what the list holds, what the loop does,
# and how each item is printed.

fruits = ["apple", "banana", "cherry", "kiwi"]

for fruit in fruits:
    print(f"I like {fruit}.")



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_datatypes.py
#    git commit -m "Completed task 3"
#    git push origin main
# -------------------------------------------



# Extension 1:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1:\n"
    + "-------------------------------------------")
# TODO:
# Add comments that describe what’s happening in this loop
# and what the variable "total" represents.

total = 0
for i in range(1, 6):
    number = int(input(f"Enter number {i}: "))
    total += number

print(f"The total is {total}")



# Extension 2:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2:\n"
    + "-------------------------------------------")
# TODO:
# Add comments to explain how this password check works.
# Focus on the while loop logic and string comparison.

password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Incorrect, try again.")

print("Access granted!")



# Extension 3:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3:\n"
    + "-------------------------------------------")
# TODO:
# Add comments explaining what’s happening at each step.
# Think about how user input is handled and what’s being counted.

count = 0
sentence = input("Type a sentence: ").lower()
for letter in sentence:
    if letter == "a":
        count += 1

print(f"The letter 'a' appears {count} times.")



# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# TODO:
# This is an optional challenge for extra practice.
# Add detailed comments describing how the menu system works,
# what each option does, and how the while loop controls the programme.

choice = ""

while choice != "3":
    print("\nMenu:")
    print("1. Count to 10")
    print("2. Show even numbers between 1–20")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for i in range(1, 11):
            print(i, end=" ")
        print()
    elif choice == "2":
        for i in range(2, 21, 2):
            print(i, end=" ")
        print()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice, please try again.")



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you have completed all required tasks:
# 1. Save your file.
# 2. Open the terminal and use Git commands to stage, commit, and push your changes.
#    (Hint: recall the commands for adding, committing, and pushing.)
# 3. Check GitHub to confirm your final version appears in your repository.
# -------------------------------------------
