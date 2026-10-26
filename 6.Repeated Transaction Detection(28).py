#  Repeated Transaction Detection
n = int(input("Enter number of transactions: "))
if n <= 0:
    print("Enter a positive number of transactions.")
else:
    ids = []
    for i in range(n):
        transaction_id = input("Enter transaction ID: ").strip()
        ids.append(transaction_id)
    duplicates_found = False
    reported = []
    for transaction_id in ids:
        count = ids.count(transaction_id)
        if count > 1 and transaction_id not in reported:
            print("Repeated ID:", transaction_id,"| Count:", count)
            reported.append(transaction_id)
            duplicates_found = True
    if not duplicates_found:
        print("No repeated transaction IDs found.")
