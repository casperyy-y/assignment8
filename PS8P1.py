def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.90  # Apply 10% discount
    return total

sum_total = 0

response = input("Do you want to enter an order? (Yes/No): ").strip().lower()
while response == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    
    total = compute_total(quantity, price)
    sum_total += total

    print(f"Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")

    response = input("Do you want to enter another order? (Yes/No): ").strip().lower()

print(f"\nSum of all totals: ${sum_total:.2f}")
