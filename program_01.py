#   Write a python program to input a string and print number of upper and lower case letter along with numbers of digits in it.
#   Coded By Prakas Rana
#   MCA in Culcutta University of Technology

# Prompt user to input a string
input_string = input("Enter a string: ")

# Initialize counters for uppercase, lowercase, and digits
uppercase_count = 0
lowercase_count = 0
digit_count = 0

# Iterate through each character in the string
for char in input_string:
    # Check if the character is an uppercase letter
    if char.isupper():
        uppercase_count += 1
    # Check if the character is a lowercase letter
    elif char.islower():
        lowercase_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1

# Print the counts
print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
print(f"Digits: {digit_count}")
