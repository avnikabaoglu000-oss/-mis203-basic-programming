```python
print("Two-Item Purchase Quote")

item1 = input("First item name: ")
quantity1 = int(input("First item quantity: "))
price1 = float(input("First item unit price: "))

item2 = input("Second item name: ")
quantity2 = int(input("Second item quantity: "))
price2 = float(input("Second item unit price: "))

delivery_fee = float(input("Delivery fee: "))
tax_percent = float(input("Tax percentage: "))

line1 = quantity1 * price1
line2 = quantity2 * price2

subtotal = line1 + line2
tax = subtotal * tax_percent / 100
final_total = subtotal + tax + delivery_fee

print()
print("=" * 40)
print("PURCHASE QUOTE")
print("=" * 40)

print(f"{item1}: {quantity1} x {price1:.2f} TRY = {line1:.2f} TRY")
print(f"{item2}: {quantity2} x {price2:.2f} TRY = {line2:.2f} TRY")
print("-" * 40)
print(f"Subtotal:       {subtotal:.2f} TRY")
print(f"Tax:            {tax:.2f} TRY")
print(f"Delivery:       {delivery_fee:.2f} TRY")
print(f"Final total:    {final_total:.2f} TRY")
print("=" * 40)
```
