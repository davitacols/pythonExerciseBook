# Item prices
banana_price = 0.49
apple_price = 0.89
orange_price = 0.59

# Quantities
banana_qty = int(input("How many bananas? "))
apple_qty = int(input("How many apples? "))
orange_qty = int(input("How many oranges? "))

# Calculations
subtotal = (banana_price * banana_qty + 
           apple_price * apple_qty + 
           orange_price * orange_qty)
tax_rate = 0.08
tax = subtotal * tax_rate
total = subtotal + tax

# Receipt
print("\n=== Shopping Receipt ===")
print(f"Bananas: ${banana_price * banana_qty:.2f}")
print(f"Apples: ${apple_price * apple_qty:.2f}")
print(f"Oranges: ${orange_price * orange_qty:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")