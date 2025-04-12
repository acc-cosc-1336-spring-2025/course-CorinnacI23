# src/homework/i_dictionaries_and_sets/dictionary.py

def add_inventory(widgets, widget_name, quantity):
    """
    Adds a widget to the inventory if it doesn't exist.
    If it exists, it updates the quantity.
    
    :param widgets: Dictionary containing the inventory items.
    :param widget_name: The name of the widget to add or update.
    :param quantity: The quantity of the widget to add or update.
    """
    if widget_name in widgets:
        widgets[widget_name] += quantity  # Update the existing widget's quantity
    else:
        widgets[widget_name] = quantity  # Add a new widget to the inventory

# src/homework/i_dictionaries_and_sets/dictionary.py

def remove_inventory_widget(widgets, widget_name):
    """
    Removes a widget from the inventory.
    
    :param widgets: Dictionary containing the inventory items.
    :param widget_name: The name of the widget to remove.
    :return: A message indicating whether the widget was deleted or not found.
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'

