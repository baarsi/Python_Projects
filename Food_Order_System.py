# Menus for Italian and Indian food options
italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

# Function to find a meal in the menu
def find_meal(name, menu):
    if name in menu:
        return name
    else:
        return None

# Function to select a meal based on food type (Italian or Indian)
def select_meal(name, food_type):
    if food_type == "Italian":
        return find_meal(name, italian_food)
    elif food_type == "Indian":
        return find_meal(name, indian_food)
    else:
        return None

# Function to display available meals based on the food type
def display_available_meals(food_type):
    if food_type == "Italian":
        print("Available Italian Meals:")
        for meal in italian_food:
            print(meal)
    elif food_type == "Indian":
        print("Available Indian Meals:")
        for meal in indian_food:
            print(meal)
    else:
        print("Invalid food type")

# Function to create a summary of the order
def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order is None:
        return "Meal not found"
    else:
        return f"You ordered {amount} {name}"

# Main order system interaction
print("Welcome to the Food Order System!")
type_input = input("What type of food do you want to choose? ")
display_available_meals(type_input)

name_input = input("Meal choice: ")
amount_input = input("Order quantity: ")

result = create_summary(name_input, amount_input, type_input)
print(result)
