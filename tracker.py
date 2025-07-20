import click
from commands.add import add_expense_command
from commands.list import list_expenses_command
from commands.summary import summary_command

@click.group()
def cli():
    """Personal Expense Tracker CLI"""
    pass

cli.add_command(add_expense_command, name="add")
cli.add_command(list_expenses_command, name="list")
cli.add_command(summary_command, name="summary")

def interactive_mode():
    from db.database import SessionLocal
    db = SessionLocal()
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ") or None
            
            from commands.add import add_expense
            try:
                expense = add_expense(db, date, category, amount, description)
                print(f"Added expense ID: {expense.id}")
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif choice == "2":
            category = input("Filter by category (leave blank for all): ") or None
            start_date = input("Start date (YYYY-MM-DD, leave blank for no filter): ") or None
            end_date = input("End date (YYYY-MM-DD, leave blank for no filter): ") or None
            
            from commands.list import get_expenses
            expenses = get_expenses(db, category, start_date, end_date)
            
            if not expenses:
                print("No expenses found.")
                continue
                
            print("\nDate       | Category      | Amount    | Description")
            print("------------------------------------------------")
            for expense in expenses:
                print(f"{expense.date} | {expense.category:13} | ${expense.amount:8.2f} | {expense.description or ''}")
                
        elif choice == "3":
            month = input("Enter month to summarize (MM, leave blank for all): ") or None
            year = input("Enter year to summarize (YYYY, leave blank for all): ") or None
            
            from commands.summary import get_summary
            summary = get_summary(db, month, int(year) if year else None)
            
            if not summary:
                print("No expenses found for the given criteria.")
                continue
                
            print("\nExpense Summary:")
            print("----------------")
            total = 0
            for category, amount in summary:
                print(f"{category:15}: ${amount:.2f}")
                total += amount
            print("----------------")
            print(f"Total: ${total:.2f}")
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
    
    db.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        cli()