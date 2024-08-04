# Example weight of the package
weight = 4.8

# Calculate and print the cost of Ground Shipping
if weight <= 2:
    cost_ground = 1.50 * weight + 20.00
elif weight <= 6:
    cost_ground = 3.00 * weight + 20.00
elif weight <= 10:
    cost_ground = 4.00 * weight + 20.00
else:
    cost_ground = 4.75 * weight + 20.00
print("Ground Shipping Cost: $", cost_ground)

# Print the cost of Ground Shipping Premium
ground_shipping_premium_cost = 125
print("Ground Shipping Premium: $", ground_shipping_premium_cost)

# Calculate and print the cost of Drone Shipping
if weight <= 2:
    cost_drone = 4.50 * weight + 0.00
elif weight <= 6:
    cost_drone = 9.00 * weight + 0.00
elif weight <= 10:
    cost_drone = 12.00 * weight + 0.00
else:
    cost_drone = 14.25 * weight + 0.00
print("Drone Shipping Cost: $", cost_drone)

