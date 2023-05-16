# Define some constants
TAX_RATE = 0.08
DISCOUNT = 0.1

# Get input from user
subtotal = float(input("Enter the subtotal: "))

# Calculate total with tax and discount
tax = subtotal * TAX_RATE
discount = subtotal * DISCOUNT
total = subtotal + tax - discount

# Print the results
print("Subtotal: ", subtotal)
print("Tax: ", tax)
print("Discount: ", discount)
print("Total: ", total)

# Use some keywords and operators
if total > 100:
    print("You get a 10% discount on your next purchase!")
else:
    print("Thanks for shopping with us!")
