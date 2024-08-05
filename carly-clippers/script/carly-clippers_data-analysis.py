# List of hairstyles offered at Carly’s Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Corresponding prices for each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of purchases for each hairstyle in the last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Initialize total price variable
total_price = 0

# Calculate the sum of all prices
for price in prices:
    total_price += price

# Compute the average price of all hairstyles
average_price = total_price / len(prices)

# Print the average price of hairstyles
print(f"Average Haircut Price: {average_price}")

# Apply a discount of $5 to each price
new_prices = [price - 5 for price in prices]

# Print the updated prices after discount
print(new_prices)

# Initialize total revenue variable
total_revenue = 0

# Calculate total revenue by iterating over the list of hairstyles
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

# Print the total revenue generated
print(f"Total Revenue: {total_revenue}")

# Calculate average daily revenue assuming 7 days in a week
average_daily_revenue = total_revenue / 7 

# Print the average daily revenue
print(f"Average Daily Revenue: {average_daily_revenue}")

# Create a list of hairstyles that cost less than $30 after discount
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Print the list of hairstyles under $30
print(cuts_under_30)

