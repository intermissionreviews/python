
    
# Get user input
user_input = input("Please enter a single character: ")

# Check if the input is a single character and a letter
if len(user_input) != 1:
    print("Error: Please enter exactly one character.")
elif not user_input.isalpha():
    print("Error: The input must be a letter.")
else:
    # Convert to lowercase to simplify checking
    char = user_input.lower()
    
    # Check if it's a vowel
    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{user_input}' is a vowel.")
    else:
        print(f"'{user_input}' is a consonant.")    