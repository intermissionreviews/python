
# Get user input for the number of rows and character
rows = int(input("Enter the number of rows: "))
character = input("Enter the character to use for the pattern: ")

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing characters in each row
    for j in range(i):
        print(character, end=' ')
    # Move to the next line after each row is printed
    print()