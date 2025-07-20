from sqlalchemy.orm import Session
from models.expense import Expense
from datetime import datetime
import click

def add_expense(db: Session, date: str, category: str, amount: float, description: str = None):
    try:
        expense_date = datetime.strptime(date, "%Y-%m-%d").date()
        new_expense = Expense(
            date=expense_date,
            category=category,
            amount=amount,
            description=description
        )
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return new_expense
    except Exception as e:
        db.rollback()
        raise e

@click.command()
@click.option('--date', required=True, help='Expense date in YYYY-MM-DD format')
@click.option('--category', required=True, help='Expense category')
@click.option('--amount', required=True, type=float, help='Expense amount')
@click.option('--description', help='Expense description')
def add_expense_command(date, category, amount, description):
    from db.database import SessionLocal
    db = SessionLocal()
    try:
        expense = add_expense(db, date, category, amount, description)
        click.echo(f"Added expense: {expense.id} - {expense.category} - ${expense.amount}")
    except Exception as e:
        click.echo(f"Error adding expense: {str(e)}", err=True)
    finally:
        db.close()