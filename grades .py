def get_valid_mark(subject_name):
    """Get a valid mark (0-100) from the user for a given subject."""
    while True:
        try:
            mark = float(input(f"Enter your mark for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Mark must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(average):
    """Determine the grade based on the average mark."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Grade Calculator")
    print("----------------")
    
    # Get marks for three subjects with validation
    subjects = ["Math", "History", "English"]
    marks = []
    
    for subject in subjects:
        mark = get_valid_mark(subject)
        marks.append(mark)
    
    # Calculate average
    average = sum(marks) / len(marks)
    
    # Determine grade
    grade = calculate_grade(average)
    
    # Display results
    print("\nResults:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]}")
    
    print(f"\nAverage: {average:.2f}")
    print(f"Grade: {grade}")
if __name__ == "__main__":
    main()

