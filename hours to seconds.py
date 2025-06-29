def get_time_duration():
    """
    Prompts user for time duration in hours with error handling.
    Ensures the input is a non-negative number.
    Returns the valid time duration as a float.
    """
    while True:
        try:
            # Prompt user for input
            time_input = input("Enter a time duration in hours: ")
            
            # Convert to float
            hours = float(time_input)
            
            # Check if the number is non-negative
            if hours < 0:
                print("Error: Please enter a non-negative number.")
                continue
            
            return hours
            
        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            return None

def convert_hours_to_minutes_seconds(hours):
    """
    Converts hours to minutes and seconds.
    Returns a tuple of (total_minutes, total_seconds).
    """
    total_minutes = hours * 60
    total_seconds = hours * 3600
    
    return total_minutes, total_seconds

def main():
    """
    Main function that orchestrates the time conversion program.
    """
    print("=== Time Duration Converter ===")
    print("This program converts hours to minutes and seconds.")
    print()
    
    # Get valid time duration from user
    hours = get_time_duration()
    
    # Handle case where user interrupted the program
    if hours is None:
        return
    
    # Convert to minutes and seconds
    minutes, seconds = convert_hours_to_minutes_seconds(hours)
    
    # Display results
    print(f"\n--- Conversion Results ---")
    print(f"Original time: {hours} hours")
    print(f"Converted to minutes: {minutes:.2f} minutes")
    print(f"Converted to seconds: {seconds:.2f} seconds")
    
    # Additional breakdown for better understanding
    if hours >= 1:
        whole_hours = int(hours)
        remaining_minutes = (hours - whole_hours) * 60
        print(f"\nBreakdown:")
        print(f"{whole_hours} hour(s) and {remaining_minutes:.2f} minutes")

if __name__ == "__main__":
    main()
