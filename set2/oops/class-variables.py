class Espresso:
    menu_type = "Drink"


# Retrieving class_variable using class name
print("Espresso.menu_type : ", Espresso.menu_type)

espresso_order = Espresso()

# Retrieving class_variable using reference_variable used for object creation
print("menu_type : ", espresso_order.menu_type)

# Changing class_variable using reference_variable used for object creation
espresso_order.menu_type = "Coffee"
print("changed value : ", espresso_order.menu_type)
