
# Input
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

# Processing
simple_interest = (principal * interest_rate * time_period) / 100

# Output
print(f"\nSimple Interest Calculation Results:")
print(f"Principal Amount: ${principal:,.2f}")
print(f"Interest Rate: {interest_rate}%")
print(f"Time Period: {time_period} years")
print(f"Simple Interest: ${simple_interest:,.2f}")