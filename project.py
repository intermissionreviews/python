def add_item(inventory):
    """Add a new item to the inventory"""
    print("\nAdd New Item")
    name = input("Enter item name: ").strip()
    
    # Check if item already exists
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Item '{name}' already exists in inventory!")
            return
    
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        category = input("Enter item category: ").strip()
        
        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity must be non-negative!")
            return
            
        new_item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'category': category
        }
        inventory.append(new_item)
        print(f"Item '{name}' added successfully!")
    except ValueError:
        print("Invalid input! Price must be a number and quantity must be an integer.")

def update_item(inventory):
    """Update an existing item in the inventory"""
    print("\nUpdate Item")
    name = input("Enter the name of the item to update: ").strip()
    
    found = False
    for item in inventory:
        if item['name'].lower() == name.lower():
            found = True
            print(f"Current details for '{name}':")
            print(f"Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
            
            try:
                price = input("Enter new price (leave blank to keep current): ").strip()
                quantity = input("Enter new quantity (leave blank to keep current): ").strip()
                category = input("Enter new category (leave blank to keep current): ").strip()
                
                if price:
                    new_price = float(price)
                    if new_price <= 0:
                        print("Price must be positive!")
                        return
                    item['price'] = new_price
                
                if quantity:
                    new_quantity = int(quantity)
                    if new_quantity < 0:
                        print("Quantity must be non-negative!")
                        return
                    item['quantity'] = new_quantity
                
                if category:
                    item['category'] = category
                
                print(f"Item '{name}' updated successfully!")
            except ValueError:
                print("Invalid input! Price must be a number and quantity must be an integer.")
            break
    
    if not found:
        print(f"Item '{name}' not found in inventory!")

def view_inventory(inventory):
    """Display all items in the inventory"""
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
        return
    
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10} {'Category':<15}")
    print("-" * 55)
    for item in inventory:
        print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10} {item['category']:<15}")

def remove_item(inventory):
    """Remove an item from the inventory"""
    print("\nRemove Item")
    name = input("Enter the name of the item to remove: ").strip()
    
    for i, item in enumerate(inventory):
        if item['name'].lower() == name.lower():
            del inventory[i]
            print(f"Item '{name}' removed successfully!")
            return
    
    print(f"Item '{name}' not found in inventory!")

def search_by_category(inventory):
    """Search for items by category"""
    print("\nSearch by Category")
    category = input("Enter the category to search for: ").strip().lower()
    
    found_items = [item for item in inventory if item['category'].lower() == category]
    
    if not found_items:
        print(f"No items found in category '{category}'.")
        return
    
    print(f"\nItems in category '{category}':")
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 40)
    for item in found_items:
        print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10}")

def main():
    """Main program loop"""
    inventory = []
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            update_item(inventory)
        elif choice == '3':
            view_inventory(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '5':
            search_by_category(inventory)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()