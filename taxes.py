amt = int(input("Cost of Item : "))
tax = int(input("Enter Tax percentage : "))
if amt>=100:
    final_cost = amt+(amt*(tax/100))
    print(f"MRP with Taxes : {final_cost}")
else:
    print(f"MRP with Taxes : {amt}")