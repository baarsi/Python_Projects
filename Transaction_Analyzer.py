# Sample transaction data with amounts and descriptions
data = [
    (749.17, "Investment Return"),
    (-11.54, "Utilities"),
    (-247.58, "Online Shopping"),
    (981.17, "Investment Return"),
    (-410.65, "Rent"),
    (310.60, "Rent"),
    (563.70, "Gift"),
    (220.79, "Salary"),
    (-49.85, "Car Maintenance"),
    (308.49, "Salary"),
    (-205.55, "Car Maintenance"),
    (870.64, "Salary"),
    (-881.51, "Utilities"),
    (518.14, "Salary"),
    (-264.66, "Groceries")
]

# Function to print all transactions
def print_transactions(transactions):
    for transaction in transactions:
        amount, statement = transaction
        print(f"${amount} - {statement}")

# Function to print a summary of total deposits, withdrawals, and balance
def print_summary(transactions):
    deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
    total_deposited = sum(deposits)
    withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    balance = total_deposited + total_withdrawn
    print(total_deposited)
    print(total_withdrawn)
    print(balance)

# Function to analyze the transactions (largest deposit/withdrawal, average, etc.)
def analyze_transactions(transactions):
    transactions.sort()
    largest_withdrawal = transactions[0]
    largest_deposit = transactions[-1]
    deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
    total_deposit = sum(deposits)
    average_deposit = total_deposit / len(deposits) if deposits else 0
    withdrawals_filter = [transaction[0] for transaction in transactions if transaction[0] < 0]
    total_withdrawals = sum(withdrawals_filter)
    average_withdrawal = total_withdrawals / len(withdrawals_filter)
    print(average_deposit)
    print(largest_withdrawal)
    print(largest_deposit)
    print(average_withdrawal)

# Main loop to let the user choose options: print summary, analyze, or stop
while True:
    choice = input("Choose between print, analyze or stop: ")
    if choice == "print":
        print_summary(data)
    elif choice == "analyze":
        analyze_transactions(data)
    elif choice == "stop":
        break
    else:
        print("Invalid choice")
