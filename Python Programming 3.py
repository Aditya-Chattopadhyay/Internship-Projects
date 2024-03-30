class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        # Add a new expense to the tracker
        self.expenses.append({'amount': amount, 'category': category, 'description': description})

    def view_monthly_summary(self, month, year):
        # View monthly summary of expenses
        monthly_expenses = [expense for expense in self.expenses if expense['date'].month == month and expense['date'].year == year]
        total_expenses = sum(expense['amount'] for expense in monthly_expenses)
        print(f"Monthly Summary for {month}/{year}: Total Expenses: ${total_expenses}")
        for category in set(expense['category'] for expense in monthly_expenses):
            category_expenses = [expense for expense in monthly_expenses if expense['category'] == category]
            category_total = sum(expense['amount'] for expense in category_expenses)
            print(f"{category}: ${category_total}")

    def view_category_expenses(self, category):
        # View expenses for a specific category
        category_expenses = [expense for expense in self.expenses if expense['category'] == category]
        if category_expenses:
            print(f"Expenses for Category '{category}':")
            for expense in category_expenses:
                print(f"${expense['amount']} - {expense['description']}")
        else:
            print(f"No expenses found for category '{category}'")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added successfully!")
        elif choice == '2':
            month = int(input("Enter month (MM): "))
            year = int(input("Enter year (YYYY): "))
            tracker.view_monthly_summary(month, year)
        elif choice == '3':
            category = input("Enter category name: ")
            tracker.view_category_expenses(category)
        elif choice == '4':
            print("Expense Tracker")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()