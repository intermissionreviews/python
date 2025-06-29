
def is_leap_year(year):
    """
    Determine if a year is a leap year.
    A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_year_input():
    """
    Get year input from user with error handling for non-numeric input.
    """
    while True:
        try:
            user_input = input("Enter a year: ").strip()
            
            # Check if input is empty
            if not user_input:
                print("Error: Please enter a valid year. Input cannot be empty.")
                continue
            
            # Convert to integer
            year = int(user_input)
            
            # Check if year is reasonable (optional validation)
            if year < 1:
                print("Error: Please enter a positive year.")
                continue
                
            return year
            
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number. Please enter a numeric year.")

def main():
    """
    Main function to run the leap year checker program.
    """
    print("=== Leap Year Checker ===")
    
    # Get year input with error handling
    year = get_year_input()
    
    # Check if it's a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
