from dictionary import add_inventory, remove_inventory_widget



def display_menu():
    """Displays the inventory menu."""
    print("\nInventory Menu")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':  # Add or Update Item
            widget_name = input("Enter widget name: ")
            quantity = int(input("Enter quantity: "))
            add_inventory(inventory, widget_name, quantity)
            print(f"Inventory updated: {widget_name} = {inventory[widget_name]}")
        
        elif choice == '2':  # Delete Item
            widget_name = input("Enter widget name to delete: ")
            message = remove_inventory_widget(inventory, widget_name)
            print(message)
        
        elif choice == '3':  # Exit
            print("Exiting inventory system.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
