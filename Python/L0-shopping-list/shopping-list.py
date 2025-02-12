# Initialize an empty shopping list
shopping_list = []

# Function to add multiple items to the shopping list
def add_items(items):
    # Split input string by commas and remove extra spaces
    item_list = [item.strip() for item in items.split(',')]
    # Extend the shopping list with the new items
    shopping_list.extend(item_list)
    print(f"{', '.join(item_list)} added to the list.")

# Function to remove multiple items from the shopping list
def remove_items(items):
    # Split input string by commas and remove extra spaces
    item_list = [item.strip() for item in items.split(',')]
    for item in item_list:
        if item in shopping_list:
            shopping_list.remove(item)  # Remove item if it exists
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")  # Notify user if item isn't found

# Function to display the shopping list
def view_list():
    print("Shopping List:")
    if shopping_list:
        for item in shopping_list:
            print(f"- {item}")  # Print each item in the list
    else:
        print("The shopping list is empty.")  # Notify if the list is empty

# Main loop to interact with the user
while True:
    # Display menu options
    print("\n1. Add Items")
    print("2. Remove Items")
    print("3. View List")
    print("4. Exit")

    # Get user input for choice
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':  # Add items
        items = input("Enter items to add (comma-separated): ")
        add_items(items)
    elif choice == '2':  # Remove items
        items = input("Enter items to remove (comma-separated): ")
        remove_items(items)
    elif choice == '3':  # View list
        view_list()
    elif choice == '4':  # Exit the program
        print("Exiting...1
              !")
              
        break
    else:
        print("Invalid choice. Please enter a valid option.")  # Handle invalid input
