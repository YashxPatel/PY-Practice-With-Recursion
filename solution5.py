# Write code for algorithm 5 below

def is_palindrome(string):
    # Remove any whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    # Reverse the string
    reversed_string = string[::-1]
    # Compare the original and reversed strings
    return string == reversed_string

input_string = input("Enter a string: ")
result = is_palindrome(input_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
