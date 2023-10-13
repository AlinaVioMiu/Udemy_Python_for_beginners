# MyWay Sandwich application
# print('Hello! Welcome to MyWay Sandwich! \nOne for 5$')
#
# toppings = ['Onions', 'Lettuce', 'Tomatoes', 'Olives', 'Peppers', 'Cheese']
# print('-----------------------------------------------')
# print('Toppings available:')
# for t in toppings:
#     print(t)
# print('You can choose three toppings.')
# t1 = input('Pick first topping:')
# t2 = input('Pick second topping:')
# t3 = input('Pick third topping:')
# print('Your sandwich has:', t1, t2, t3)
# print('How many sandwiches do you want to buy?')
# how_many = int(input())
# total_cost = 5 * how_many
# print('Total cost =', total_cost, '$')

# toppings = [x for x in input("Please pick three of the following toppings for your sandwiches (onions, lettuce, tomato, peppers, olives) and seperate them by comma: ").split(",")]
# sandwich_num = int(input("How many sandwiches would you like to purchase for five dollars each? "))
# cost = sandwich_num*5
# print(f"Your total is {cost} dollars.")
# print(f"You will receive {sandwich_num} sandwiches with the following toppings: {toppings}")


toppings = {
    "Cheese": 1.50,
    "Lettuce": 0.75,
    "Tomato": 0.50,
    "Onion": 0.50,
    "Bacon": 2.00,
}

# Initialize an empty list to store the selected toppings
selected_toppings = []

# Prompt the user to select 3 toppings
print("Select 3 toppings for your burger:")
while len(selected_toppings) < 3:
    print("Available toppings:")
    for topping, cost in toppings.items():
        if topping not in selected_toppings:
            print(f"{topping}: ${cost}")

    choice = input("Enter the name of a topping: ")

    # Check if the topping is valid and not already selected
    if choice in toppings and choice not in selected_toppings:
        selected_toppings.append(choice)
    else:
        print("Invalid choice or topping already selected. Try again.")

# Calculate the total cost
total_cost = sum(toppings[topping] for topping in selected_toppings)

# Display the selected toppings and the total bill
print("\nSelected Toppings:")
for topping in selected_toppings:
    print(f"{topping}: ${toppings[topping]}")
print(f"Total Bill: ${total_cost:.2f}")