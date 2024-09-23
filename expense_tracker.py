
# Expense Tracker

# Global list to hold expenses
expenses = []

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category (e.g., food, travel, etc.): ")
        expense = {
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

# Function to view all expenses and calculate total spending
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        total_spending = 0
        print("\n--- All Expenses ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Amount: {expense['amount']}, Category: {expense['category']}")
            total_spending += expense['amount']
        print(f"\nTotal Spending: {total_spending:.2f}\n")

# Function to save expenses to a file
def save_expenses():
    with open("expenses.txt", "w") as file:
        if not expenses:
            file.write("No expenses recorded yet.")
        else:
            for expense in expenses:
                file.write(f"Amount: {expense['amount']}, Category: {expense['category']}\n")
            total_spending = sum(expense['amount'] for expense in expenses)
            file.write(f"\nTotal Spending: {total_spending:.2f}\n")
    print("Expenses saved to 'expenses.txt'.")

# Main program loop
def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Save Expenses to File")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
