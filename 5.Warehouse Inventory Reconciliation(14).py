# Warehouse Inventory Reconciliation
n = int(input("Enter number of inventory items: "))
if n <= 0:
    print("Enter a positive number of items.")
else:
    shortage = 0
    surplus = 0
    matched = 0
    for i in range(1, n + 1):
        print("\nItem", i)
        name = input("Enter item name: ")
        expected = int(input("Enter expected quantity: "))
        physical = int(input("Enter physical quantity: "))
        if expected < 0 or physical < 0:
            print("Quantities cannot be negative. Item skipped.")
            continue
        difference = physical - expected
        if difference < 0:
            status = "Shortage"
            shortage += 1
        elif difference > 0:
            status = "Surplus"
            surplus += 1
        else:
            status = "Matched"
            matched += 1
        print("Item:", name)
        print("Difference:", difference)
        print("Status:", status)
    print("\nInventory Summary")
    print("Shortage items:", shortage)
    print("Surplus items:", surplus)
    print("Matched items:", matched)
