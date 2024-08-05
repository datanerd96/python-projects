# list for toppings

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# list for the prices

prices = [2, 6, 1, 3, 2, 7, 2]

# how many 2 dollar slices are there?

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# number of pizzas

num_pizzas = len(toppings)
print(num_pizzas)

# Printing the amount of pizzas

print(f"We sell {num_pizzas} different kinds of pizza!")

# Combining the 2 lists

pizza_and_prices = [[x, y] for x in prices for y in toppings]

# Printing new list
print(pizza_and_prices)

pizza_and_prices.sort()

# Storing first element in cheapest_pizza

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# The most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# The most expensive pizza was bought
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Adding a new topping and price

pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

# Giving away three cheapest pizza

pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[3:]
print(three_cheapest)


