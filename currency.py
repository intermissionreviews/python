
# Define exchange rates for target currencies (these rates are hypothetical)
USD_TO_EUR = 0.85  # 1 USD = 0.85 EUR
USD_TO_GBP = 0.75  # 1 USD = 0.75 GBP
USD_TO_JPY = 110.0 # 1 USD = 110.0 JPY

# Function to perform currency conversion
def convert_currency(amount, target_currency):
    """Convert USD to the specified target currency."""
    if target_currency == '1':
        converted_amount = amount * USD_TO_EUR
        print(f"Converted amount in EUR: €{converted_amount:.2f}")
    elif target_currency == '2':
        converted_amount = amount * USD_TO_GBP
        print(f"Converted amount in GBP: £{converted_amount:.2f}")
    elif target_currency == '3':
        converted_amount = amount * USD_TO_JPY
        print(f"Converted amount in JPY: ¥{converted_amount:.2f}")
    else:
        print("Invalid currency selection. Please choose 1, 2, or 3.")

# Get user input for the amount in USD
amount_in_usd = float(input("Enter the amount in USD: "))

# Get user input for the target currency
print("Select target currency (1 for EUR, 2 for GBP, 3 for JPY): ")
target_currency = input("Enter the number corresponding to the target currency: ")

# Perform the conversion
convert_currency(amount_in_usd, target_currency)