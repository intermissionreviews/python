def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
