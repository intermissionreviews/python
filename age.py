def classify_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Error: Age cannot be negative. Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid positive integer for age.")
    
    if age < 18:
        category = "Minor"
    elif 18 <= age <= 65:
        category = "Adult"
    else:
        category = "Senior citizen"
    
    print(f"Your age category is: {category}")
    
    # Run the function
classify_age()
