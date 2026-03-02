"# -------------------------------------------
# Exercise 2: Documentation & System Logic
# -------------------------------------------
#
# GOAL:
# 1. Master Commenting: Learn to explain 'what' and 'why' code runs.
# 2. Understand System Logic: Deconstruct inputs, conditions, and loops.
# 3. Practise the Core Git Workflow: Stage -> Commit -> Push.
#
# CONCEPT:
# In professional environments, code is read more often than it is written. 
# Using "#" allows you to leave notes for yourself and others.
# Good documentation is the difference between a broken system and a working one.
#
# -------------------------------------------


# -------------------------------------------
# Task 1: Logging User Details
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Logging User Details\n"
    + "-------------------------------------------")

# CONCEPT: Documentation.
# Use comments to describe the data being captured.

# TODO:
# The code below captures personal details. 
# 1. Add a comment above each line explaining what it does.
# 2. Add one "Header Comment" at the top explaining the overall goal of this task.

# Write your comments below:

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")


# -------------------------------------------
# Task 2: Environmental Monitoring (Logic)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Environmental Monitoring\n"
    + "-------------------------------------------")

# CONCEPT: Logical Branching.
# Comments should explain why specific thresholds (like 30 or 15) are chosen.

# TODO:
# 1. Read the code below.
# 2. Add comments to explain what each 'if/elif/else' block is checking for.
# 3. Explain why we use 'float()' for temperature instead of 'int()'.

# Write your comments below:

temperature = float(input("Enter the current temperature in °C: "))

if temperature > 30:
    print("Threshold exceeded! Alert: High Temperature.")
elif temperature >= 15:
    print("Temperature within normal operating range.")
else:
    print("Alert: Low Temperature. Heating required.")


# -------------------------------------------
# Task 3: Iterating Through Records (Loops)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Iterating Through Records\n"
    + "-------------------------------------------")

# CONCEPT: For Loops.
# Comments help track how data moves from a list into a variable.

# TODO:
# 1. Add comments explaining what the 'fruits' list represents in a system.
# 2. Explain how the 'for fruit in fruits' loop processes each item one by one.

# Write your comments below:

fruits = ["apple", "banana", "cherry", "kiwi"]

for fruit in fruits:
    print(f"Item processed: {fruit}.")


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Core Tasks. Let's save.
# 1. Save this file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex2_comments.py
#    git commit -m "Completed core documentation tasks"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Running Totals
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: Running Totals\n"
    + "-------------------------------------------")

# TODO:
# 1. Add comments to explain how the 'total' variable changes inside the loop.
# 2. Explain what 'range(1, 6)' does in this context.

total = 0
for i in range(1, 6):
    number = int(input(f"Enter reading {i}: "))
    total += number

print(f"Final System Total: {total}")


# Extension 2: Security & Access Logic
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Security & Access Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Add comments explaining the 'while' loop condition.
# 2. Explain why we check 'if password != "python123"' inside the loop.

password = ""
while password != "python123":
    password = input("Enter system password: ")
    if password != "python123":
        print("Access Denied. Try again.")

print("Access Granted!")


# Extension 3: Letter Frequency Counter
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: Letter Frequency Counter\n"
    + "-------------------------------------------")

# TODO:
# 1. Add comments explaining what’s happening at each step.
# 2. Explain how user input is handled (normalised) and what’s being counted.

count = 0
sentence = input("Type a sentence: ").lower()
for letter in sentence:
    if letter == "a":
        count += 1

print(f"The letter 'a' appears {count} times.")


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Extensions. Let's save.
# 1. Save this file.
# 2. Run:
#    git add Ex2_comments.py
#    git commit -m "Completed documentation extensions"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: System Menu Navigation
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: System Menu Navigation\n"
    + "-------------------------------------------")

# TODO:
# 1. This menu allows users to interact with system tools.
# 2. Add detailed comments explaining how the 'while choice != "3"' loop works.
# 3. Comment on each menu option to explain the output and logic.

choice = ""

while choice != "3":
    print("\nSystem Control Menu:")
    print("1. Run 10-count Diagnostic")
    print("2. Display Even Range (1-20)")
    print("3. Log Out")
    choice = input("Select an option: ")

    if choice == "1":
        for i in range(1, 11):
            print(i, end=" ")
        print()
    elif choice == "2":
        for i in range(2, 21, 2):
            print(i, end=" ")
        print()
    elif choice == "3":
        print("Logging out of system...")
    else:
        print("Invalid selection.")


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex2_comments.py
#    git commit -m "Completed all documentation activities"
#    git push origin main
# -------------------------------------------"
